from player import Player

from game import (
    number_guessing,
    prime_challenge,
    fibonacci_challenge
)

from scoring import display_score
from statistics import show_statistics, performance_message

from utils import (
    display_title,
    get_player_name,
    get_menu_choice
)


def main():

    display_title()

    name = get_player_name()

    player = Player(name)

    print(f"\nWelcome, {player.name}!")
    print("Let's begin your Number Quest.\n")

    while True:

        choice = get_menu_choice()

        if choice == "1":
            number_guessing(player)

        elif choice == "2":
            prime_challenge(player)

        elif choice == "3":
            fibonacci_challenge(player)

        elif choice == "4":
            display_score(player)

        elif choice == "5":
            show_statistics(player)

            print(performance_message(player))

        elif choice == "6":
            print("\n===================================")
            print(f"Thanks for playing, {player.name}!")
            print(f"Final Score: {player.score}")
            print(f"Accuracy: {player.get_accuracy():.2f}%")
            print("===================================")

            break


if __name__ == "__main__":
    main()
