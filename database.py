import sqlite3
import json
import hashlib

def connect():
    return sqlite3.connect("text_game.db")

def create_user_table():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS saves (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                current_room TEXT NOT NULL,
                inventory TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """)

def register_user(username, password):
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    try:
        with connect() as conn:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?);", (username, hashed_pw))
        return True
    except sqlite3.IntegrityError:
        return False

def authenticate_user(username, password):
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    with connect() as conn:
        cursor = conn.execute("SELECT id FROM users WHERE username = ? AND password = ?;", (username, hashed_pw))
        result = cursor.fetchone()
        return result[0] if result else None

def save_game(user_id, current_room, inventory):
    inventory_json = json.dumps(inventory)
    with connect() as conn:
        cursor = conn.execute("SELECT id FROM saves WHERE user_id = ?;", (user_id,))
        if cursor.fetchone():
            conn.execute("UPDATE saves SET current_room = ?, inventory = ? WHERE user_id = ?;",
                         (current_room, inventory_json, user_id))
        else:
            conn.execute("INSERT INTO saves (user_id, current_room, inventory) VALUES (?, ?, ?);",
                         (user_id, current_room, inventory_json))

def load_game(user_id):
    with connect() as conn:
        cursor = conn.execute("SELECT current_room, inventory FROM saves WHERE user_id = ?;", (user_id,))
        result = cursor.fetchone()
        if result:
            return {
                "current_room": result[0],
                "inventory": json.loads(result[1])
            }
        return None

def setup_rooms():
    with connect() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description_with_item TEXT,
            description_no_item TEXT
        );
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_name TEXT NOT NULL,
            item_name TEXT NOT NULL,
            FOREIGN KEY (room_name) REFERENCES rooms(name)
        );
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS connections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_room TEXT NOT NULL,
            direction TEXT CHECK (direction IN ('north', 'south', 'east', 'west')) NOT NULL,
            to_room TEXT NOT NULL,
            FOREIGN KEY (from_room) REFERENCES rooms(name),
            FOREIGN KEY (to_room) REFERENCES rooms(name)
        );
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS crafting (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient1 TEXT NOT NULL,
            ingredient2 TEXT NOT NULL,
            result TEXT NOT NULL
        );
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS room_unlocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_name TEXT NOT NULL,
            requirement_type TEXT CHECK (requirement_type IN ('item', 'crafted')) NOT NULL,
            requirement_value TEXT NOT NULL,
            locked_description TEXT
        );
        """)

def populate_rooms():
    rooms = {
        'Decrepit Entrance': {
            'description_with_item': "The entryway creaks beneath your boots. A scorched circuit board lies half-buried in dust.",
            'description_no_item': "The lights flicker, but there's nothing left here.",
            'item': 'Circuit Board',
            'connections': {'south': 'Entrance Hall'}
        },
        'Entrance Hall': {
            'description_with_item': "A grand but lifeless chamber. Something metallic glints beneath debris.",
            'description_no_item': "The hall is empty and echoes with your steps.",
            'item': 'Battery',
            'connections': {'north': 'Decrepit Entrance', 'east': 'Canteen', 'west': 'Laboratory'}
        },
        'Laboratory': {
            'description_with_item': "Amid overturned stools, a syringe gleams under flickering light.",
            'description_no_item': "The lab is sterile and picked clean.",
            'item': 'Syringe',
            'connections': {'east': 'Entrance Hall', 'south': 'Supply Closet'}
        },
        'Supply Closet': {
            'description_with_item': "A rusted toolbox peeks from under planks.",
            'description_no_item': "Empty shelves creak in the stale air.",
            'item': 'Toolbox',
            'connections': {'north': 'Laboratory'}
        },
        'Canteen': {
            'description_with_item': "Near a shattered vending machine, a protein bar rests.",
            'description_no_item': "The air is thick with mold. Nothing remains.",
            'item': 'Protein Bar',
            'connections': {'west': 'Entrance Hall', 'south': 'Abandoned Office'}
        },
        'Abandoned Office': {
            'description_with_item': "A keycard lies under a shattered monitor.",
            'description_no_item': "Desks are cleared, files scattered.",
            'item': 'Keycard',
            'connections': {'north': 'Canteen', 'south': 'Meeting Room'}
        },
        'Meeting Room': {
            'description_with_item': "A folder of worn blueprints flutters in the breeze.",
            'description_no_item': "Papers litter the floor. The projector is smashed.",
            'item': 'Blueprint',
            'connections': {'north': 'Abandoned Office', 'south': 'Tech Center'}
        },
        'Tech Center': {
            'description_with_item': "A portable hard drive buzzes softly in a docking station.",
            'description_no_item': "Screens show data loops. You already took the drive.",
            'item': 'Hard Drive',
            'connections': {'north': 'Meeting Room', 'west': 'Backup Servers', 'east': 'Server Room'}
        },
        'Backup Servers': {
            'description_with_item': "One server emits a soft glow—its firewall module intact.",
            'description_no_item': "The backup units are cold and quiet.",
            'item': 'Firewall Module',
            'connections': {'east': 'Tech Center'}
        },
        'Server Room': {
            'description_with_item': "A massive terminal looms ahead. Alphamind awaits.",
            'description_no_item': "The server array is alive, whispering of your fate.",
            'item': None,
            'connections': {'west': 'Tech Center'}
        }
    }

    crafting_recipes = [
        ("Circuit Board", "Battery", "Power Core"),
        ("Toolbox", "Syringe", "Injector"),
        ("Blueprint", "Hard Drive", "System Patch"),
        ("Firewall Module", "Keycard", "Security Override"),
        ("Protein Bar", "Injector", "Rejuvenation Kit")
    ]

    room_unlocks = [
        ("Backup Servers", "crafted", "System Patch", "The backup server door remains locked, unresponsive."),
        ("Server Room", "crafted", "Security Override", "You swipe the keycard, but the system denies access."),
        ("Server Room", "crafted", "Power Core", "The server needs power to delete Alphamind."),
    ]

    with connect() as conn:
        for name, data in rooms.items():
            conn.execute("""INSERT OR IGNORE INTO rooms (name, description_with_item, description_no_item)
                            VALUES (?, ?, ?);""", (name, data['description_with_item'], data['description_no_item']))
            if data['item']:
                conn.execute("INSERT OR IGNORE INTO items (room_name, item_name) VALUES (?, ?);", (name, data['item']))
            for direction, to_room in data['connections'].items():
                conn.execute("INSERT OR IGNORE INTO connections (from_room, direction, to_room)VALUES (?, ?, ?);", (name, direction, to_room))

        for i1, i2, result in crafting_recipes:
            conn.execute("INSERT OR IGNORE INTO crafting (ingredient1, ingredient2, result) VALUES (?, ?, ?);", (i1, i2, result))

        for room, req_type, value, desc in room_unlocks:
            conn.execute("""INSERT OR IGNORE INTO room_unlocks (room_name, requirement_type, requirement_value, locked_description)
                            VALUES (?, ?, ?, ?);""", (room, req_type, value, desc))

def get_craft_result(item1, item2):
    with connect() as conn:
        cursor = conn.execute("""
            SELECT result FROM crafting
            WHERE (ingredient1 = ? AND ingredient2 = ?)
               OR (ingredient1 = ? AND ingredient2 = ?)
        """, (item1, item2, item2, item1))
        result = cursor.fetchone()
        return result[0] if result else None

def is_room_locked(room_name, inventory):
    with connect() as conn:
        cursor = conn.execute("""
            SELECT requirement_type, requirement_value, locked_description
            FROM room_unlocks
            WHERE room_name = ?;
        """, (room_name,))
        locks = cursor.fetchall()

        for req_type, req_value, _ in locks:
            if req_type == "crafted" or req_type == "item":
                if req_value not in inventory:
                    return True
        return False

def get_locked_description(room_name, inventory):
    with connect() as conn:
        cursor = conn.execute("""
            SELECT requirement_type, requirement_value, locked_description
            FROM room_unlocks
            WHERE room_name = ?;
        """, (room_name,))
        for req_type, req_value, desc in cursor.fetchall():
            if req_value not in inventory:
                return desc
        return None
