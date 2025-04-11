"""Adventure Game Module

This module contains the functionality to play the Lost Temple of Data adventure game.
It provides options to start the adventure or exit the game.
"""

def start_adventure():
    """Starts the adventure game by displaying the introduction and options to the player."""
    print("Welcome to the Lost Temple of Data!")
    print("You are about to embark on an exciting adventure.")
    print("1. Start Adventure")
    print("2. Exit")

def choose_path(choice):
    """Chooses the path based on the player's input.

    If the choice is 1, the player takes the adventurous path.
    If the choice is 2, the player chooses to exit the game.
    """
    if choice == 1:
        print("You have chosen the adventurous path!")
    elif choice == 2:
        print("You have chosen to exit the game. Goodbye!")

def main():
    """Main function to run the game."""
    start_adventure()  # Display the introduction and options to the player.
    try:
        choice = int(input("Enter your choice: "))  # Get the player's choice.
        if choice not in [1, 2]:
            raise ValueError("Invalid choice. Please enter 1 or 2.")
    except ValueError as e:
        print(e)
        return
    choose_path(choice)  # Process the player's choice.

# Run the main function if this script is executed.
if __name__ == "__main__":
    main()  # Start the adventure game.