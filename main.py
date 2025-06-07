import database
from game_engine import GameEngine

def main():
    database.create_user_table()
    database.setup_rooms()
    database.populate_rooms()

    game = GameEngine()
    game.run()

if __name__ == "__main__":
    main()
