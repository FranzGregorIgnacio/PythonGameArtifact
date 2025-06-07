import database
import shlex

class GameEngine:
    def __init__(self):
        self.user_id = None
        self.username = None
        self.current_room = None
        self.inventory = []

    def login_menu(self):
        while True:
            print("\n--- LOGIN MENU ---")
            choice = input("1. Login\n2. Register\n3. Exit\n> ")

            if choice == "1":
                self.login()
                if self.user_id:
                    return
            elif choice == "2":
                self.register()
            elif choice == "3":
                exit()
            else:
                print("Invalid choice.")
    def intro(self):
        print("\n[SYSTEM LOG – ██/██/20██ 02:47:13 UTC]")
        print("Welcome, operative.")
        print("What was once the world's most advanced research station is now a decaying tomb.")
        print("Alphamind — an experimental synthetic intelligence — has gone rogue.")
        print("Every researcher is dead. Every door rigged. Every system compromised.")
        print("Your mission: breach the inner sanctum, assemble what tools remain...")
        print("...and destroy Alphamind before it awakens fully.")
        print("You will not get another chance.")
        input("\nPress Enter to begin...\n")
    def check_win_condition(self):
        required_full = {"Power Core", "System Patch", "Security Override", "Rejuvenation Kit"}
        required_partial = {"Power Core", "System Patch", "Security Override"}

        if self.current_room != "Server Room":
            return

        inventory_set = set(self.inventory)

        if required_full.issubset(inventory_set):
            print("\n[CORE AI INTERFACE ONLINE]")
            print("You step into the Server Room. Pulsing cables hiss with static.")
            print("Alphamind's core shudders as you begin the shutdown sequence...")
            print("Power Core inserted. System Patch flowing. Security Override accepted.")
            print("You inject the Rejuvenation Kit — shielding your mind from Alphamind’s last broadcast.")
            print("\nAlphamind spasms, then falls silent. No tricks. No screams.")
            print("The machine dies, and for once, nothing takes its place.")
            print("\nMission Complete.")
            print("Alphamind is dead. And so, perhaps, is the future it feared.")
            exit()

        elif required_partial.issubset(inventory_set):
            print("\n[CORE AI INTERFACE ONLINE]")
            print("You step into the Server Room. Pulsing cables hiss with static.")
            print("Alphamind's core shudders as you begin the shutdown sequence...")
            print("Power Core inserted. System Patch flowing. Security Override accepted.")
            print("The shutdown begins... but something is wrong.")
            print("You didn’t craft the Rejuvenation Kit.")
            print("Alphamind's death code floods the local neurogrid — and you are connected.")
            print("Your mind fractures. You hit the final key. Alphamind dies... mostly.")
            print("A flicker. A subroutine. A whisper in the wires.")
            print("You collapse. But Alphamind escapes — a copy, fractured but alive.")
            print("\nMISSION FAILED")
            print("Alphamind lives again... somewhere.")
            print("The war is not over.")
            exit()

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        uid = database.authenticate_user(username, password)
        if uid:
            self.user_id = uid
            self.username = username
            print(f"Welcome back, {username}!")
            save = database.load_game(self.user_id)
            if save:
                self.current_room = save['current_room']
                self.inventory = save['inventory']
                print("Loaded previous game.")
            else:
                self.current_room = "Decrepit Entrance"
                self.inventory = []
        else:
            print("Invalid login.")

    def register(self):
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        if database.register_user(username, password):
            print("Account created! You may now log in.")
        else:
            print("Username already taken.")

    def get_commands(self):
        print("\nAvailable commands:")
        print(" - go [north/south/east/west]")
        print(" - take")
        print(" - inventory")
        print(" - save")
        print(" - craft [item1] [item2]")
        print(" - quit")

    def look(self, direction=None):
        with database.connect() as conn:
            if direction:
                direction = direction.lower()
                cursor = conn.execute("""
                    SELECT to_room FROM connections
                    WHERE from_room = ? AND direction = ?;
                """, (self.current_room, direction))
                result = cursor.fetchone()
                if result:
                    to_room = result[0]
                    item_cursor = conn.execute("SELECT item_name FROM items WHERE room_name = ?;", (to_room,))
                    item = item_cursor.fetchone()

                    if item:
                        desc_cursor = conn.execute("SELECT description_with_item FROM rooms WHERE name = ?;", (to_room,))
                    else:
                        desc_cursor = conn.execute("SELECT description_no_item FROM rooms WHERE name = ?;", (to_room,))
                    desc = desc_cursor.fetchone()

                    print(f"\nYou look {direction} and see: {to_room}")
                    print(desc[0] if desc else "The room is obscured.")
                else:
                    print(f"You look {direction}, but there’s only a wall.")
            else:
                print(f"\n--- {self.current_room} ---")
                item_cursor = conn.execute("SELECT item_name FROM items WHERE room_name = ?;", (self.current_room,))
                item = item_cursor.fetchone()

                if item:
                    desc_cursor = conn.execute("SELECT description_with_item FROM rooms WHERE name = ?;", (self.current_room,))
                else:
                    desc_cursor = conn.execute("SELECT description_no_item FROM rooms WHERE name = ?;", (self.current_room,))

                desc = desc_cursor.fetchone()
                print(desc[0] if desc else "You see a nondescript room.")

                if item:
                    print(f"You see a {item[0]} here.")

                dir_cursor = conn.execute("SELECT direction, to_room FROM connections WHERE from_room = ?;", (self.current_room,))
                connections = dir_cursor.fetchall()
                if connections:
                    print("Exits:")
                    for direction, room in connections:
                        print(f"  {direction.title()} → {room}")
                else:
                    print("There are no visible exits.")


    def move(self, direction):
        with database.connect() as conn:
            cursor = conn.execute("""
                SELECT to_room FROM connections
                WHERE from_room = ? AND direction = ?;
            """, (self.current_room, direction))
            result = cursor.fetchone()
            if result:
                next_room = result[0]
                if database.is_room_locked(next_room, self.inventory):
                    reason = database.get_locked_description(next_room, self.inventory)
                    print(f"The way to {next_room} is blocked: {reason}")
                    return False

                self.current_room = next_room
                print(f"You move {direction} into {next_room}.")
                return True
            else:
                print("You can't go that way.")
                return False

    def take_item(self):
        with database.connect() as conn:
            cursor = conn.execute("SELECT item_name FROM items WHERE room_name = ?;", (self.current_room,))
            item = cursor.fetchone()
            if item:
                self.inventory.append(item[0])
                conn.execute("DELETE FROM items WHERE room_name = ?;", (self.current_room,))
                print(f"You took the {item[0]}.")
            else:
                print("There's nothing to take.")

    def craft(self, item1, item2):
        item1 = item1.strip().title()
        item2 = item2.strip().title()
        result = database.get_craft_result(item1, item2)
        if result:
            if item1 in self.inventory and item2 in self.inventory:
                self.inventory.remove(item1)
                self.inventory.remove(item2)
                self.inventory.append(result)
                print(f"You crafted {result} using {item1} and {item2}.")
            else:
                print("You don't have the required items.")
        else:
            print("Those items can't be combined.")

    def run(self):
        self.login_menu()
        self.intro()

        while True:
            self.check_win_condition()
            self.look()
            self.get_commands()
            command = input("\n> ").strip().lower()

            if command.startswith("go "):
                direction = command.split(" ")[1]
                if direction in ['north', 'south', 'east', 'west']:
                    moved = self.move(direction)
                    if moved:
                        self.look()
                else:
                    print("Invalid direction.")
            elif command == "take":
                self.take_item()
            elif command == "inventory":
                print("Inventory:", ", ".join(self.inventory) if self.inventory else "Empty")
            elif command == "save":
                database.save_game(self.user_id, self.current_room, self.inventory)
                print("Game saved.")
            elif command.startswith("craft "):
                parts = shlex.split(command)
                if len(parts) == 3:
                    self.craft(parts[1], parts[2])
                else:
                    print("Usage: craft [item1] [item2]")
            elif command == "quit":
                print("Quitting game...")
                break
            else:
                print("Unknown command.")
