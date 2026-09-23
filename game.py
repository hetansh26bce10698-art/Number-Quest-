from questions import (
    generate_number_guess,
    generate_prime_question,
    generate_fibonacci_question
)

from scoring import calculate_points
from utils import get_integer


def number_guessing(player):
    print("\n========== NUMBER GUESSING ==========")

    question = generate_number_guess()
    answer = question["answer"]

    attempts = 5

    print(question["question"])
    print(f"You have {attempts} attempts.")

    for attempt in range(1, attempts + 1):

        guess = get_integer(f"Attempt {attempt}: ")

        if guess == answer:
            print("Correct! You guessed the number.")

            player.record_answer(True)
            player.add_score(calculate_points(True, "normal"))

            return

        elif guess < answer:
            print("Too low.")

        else:
            print("Too high.")

    print(f"Sorry! The correct number was {answer}.")

    player.record_answer(False)


def prime_challenge(player):
    print("\n========== PRIME CHALLENGE ==========")

    question = generate_prime_question()

    print(question["question"])

    answer = input("Your answer: ").strip().lower()

    user_answer = answer == "yes"

    if user_answer == question["answer"]:
        print("Correct!")

        player.record_answer(True)
        player.add_score(calculate_points(True, "normal"))

    else:
        print("Incorrect.")

        correct_answer = "yes" if question["answer"] else "no"

        print(f"The correct answer was {correct_answer}.")

        player.record_answer(False)


def fibonacci_challenge(player):
    print("\n========== FIBONACCI CHALLENGE ==========")

    question = generate_fibonacci_question()

    print(question["question"])

    answer = get_integer("Your answer: ")

    if answer == question["answer"]:
        print("Correct!")

        player.record_answer(True)
        player.add_score(calculate_points(True, "hard"))

    else:
        print("Incorrect.")

        print(f"The correct answer was {question['answer']}.")

        player.record_answer(False)
