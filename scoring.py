def calculate_points(correct, difficulty="normal"):
    if not correct:
        return 0

    if difficulty == "easy":
        return 10

    if difficulty == "hard":
        return 30

    return 20


def display_score(player):
    print("\n========== SCORE ==========")
    print(f"Player: {player.name}")
    print(f"Score: {player.score}")
    print(f"Questions Answered: {player.questions_answered}")
    print(f"Correct Answers: {player.correct_answers}")
    print(f"Accuracy: {player.get_accuracy():.2f}%")
    print("===========================\n")
