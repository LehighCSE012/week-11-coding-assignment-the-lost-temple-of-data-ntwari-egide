def start_adventure():
    # Starts the adventure game by displaying the introduction and options to the player.
    print("Welcome to the Lost Temple of Data!")
    print("You are about to embark on an exciting adventure.")
    print("1. Start Adventure")
    print("2. Exit")

def choose_path(choice):
    # Chooses the path based on the player's input.
    # If the choice is 1, the player takes the adventurous path.
    # If the choice is 2, the player chooses to exit the game.
    if choice == 1:
        print("You have chosen the adventurous path!")
    elif choice == 2:
        print("You have chosen to exit the game. Goodbye!")

def main():
    # Main function to run the game.
    start_adventure()  # Display the introduction and options to the player.
    choice = int(input("Enter your choice: "))  # Get the player's choice.
    choose_path(choice)  # Process the player's choice.

# Run the main function if this script is executed.
if __name__ == "__main__":
    main()  # Start the adventure game.