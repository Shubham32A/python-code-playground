# Game: Text Adventure
# Setting: A dark, spooky forest
# Main character: A brave adventurer
# Goal: Find the hidden treasure

# Initialize player's location
current_location = "forest entrance"

# Main game loop
while True:
    print(f"You are in the {current_location}.")
    print("What do you want to do? (Type 'help' for options)")

    # Get player input
    user_input = input("> ").lower()

    if user_input == "help":
        print("Available commands:")
        print("- 'look': Examine your surroundings")
        print("- 'move <direction>': Move to a different location (e.g., 'move north')")
        print("- 'quit': Quit the game")
    elif user_input == "look":
        if current_location == "forest entrance":
            print("You see tall trees and hear rustling leaves.")
        # Add more descriptions for other locations
        # ...

    elif user_input.startswith("move "):
        direction = user_input.split()[1]
        # Implement logic to move to different locations based on direction
        # ...

    elif user_input == "quit":
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid command. Type 'help' for options.")

# End of game loop
