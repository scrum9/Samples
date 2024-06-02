class SimpleGame:
    def __init__(self):
        pass

    def start_game(self):
        print("Welcome to the Dungeons and Dragons Adventure!")
        self.first_encounter()

    def first_encounter(self):
        print("\nYou are standing at the entrance of a dark cave.")
        print("1. Enter the cave.")
        print("2. Walk away.")
        choice = input("What do you do? (1/2): ")

        if choice == "1":
            self.enter_cave()
        elif choice == "2":
            self.walk_away()
        else:
            print("Invalid choice. Try again.")
            self.first_encounter()

    def enter_cave(self):
        print("\nYou enter the cave and find a treasure chest!")
        print("1. Open the chest.")
        print("2. Ignore the chest.")
        choice = input("What do you do? (1/2): ")

        if choice == "1":
            print("You open the chest and find a magical artifact!")
        elif choice == "2":
            print("You ignore the chest and continue exploring.")
        else:
            print("Invalid choice. Try again.")
            self.enter_cave()

        self.second_encounter()

    def walk_away(self):
        print("\nYou walk away from the cave and find a small village.")
        print("1. Talk to the villagers.")
        print("2. Keep walking.")
        choice = input("What do you do? (1/2): ")

        if choice == "1":
            print("The villagers welcome you and offer you a place to stay for the night.")
        elif choice == "2":
            print("You keep walking and find a peaceful meadow to rest in.")
        else:
            print("Invalid choice. Try again.")
            self.walk_away()

        self.second_encounter()

    def second_encounter(self):
        print("\nAfter your previous adventure, you continue your journey and find a river.")
        print("1. Swim across the river.")
        print("2. Look for a bridge.")
        choice = input("What do you do? (1/2): ")

        if choice == "1":
            print("You swim across the river and reach the other side safely.")
        elif choice == "2":
            print("You find a bridge and safely cross the river.")
        else:
            print("Invalid choice. Try again.")
            self.second_encounter()

        print("\nYour adventure continues...")

if __name__ == "__main__":
    game = SimpleGame()
    game.start_game()
