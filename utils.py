def display_title():
    print("\n===================================")
    print("          NUMBER QUEST")
    print("   A Python Problem-Solving Game")
    print("===================================\n")


def get_player_name():
    while True:
        name = input("Enter your name: ").strip()

        if name:
            return name

        print("Name cannot be empty. Please try again.")


def get_menu_choice():
    print("\n========== MAIN MENU ==========")
    print("1. Number Guessing")
    print("2. Prime Challenge")
    print("3. Fibonacci Challenge")
    print("4. View Score")
    print("5. View Statistics")
    print("6. Exit")
    print("===============================")

    while True:
        choice = input("Enter your choice: ").strip()

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice

        print("Invalid choice. Please enter a number from 1 to 6.")


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            print("Invalid input. Please enter a number.")
