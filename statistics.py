def show_statistics(player):
    print("\n========== PERFORMANCE ==========")

    print(f"Player Name       : {player.name}")
    print(f"Questions Played  : {player.questions_answered}")
    print(f"Correct Answers   : {player.correct_answers}")
    print(f"Wrong Answers     : "
          f"{player.questions_answered - player.correct_answers}")

    print(f"Final Score       : {player.score}")
    print(f"Accuracy          : {player.get_accuracy():.2f}%")

    print("=================================\n")


def performance_message(player):
    accuracy = player.get_accuracy()

    if accuracy >= 80:
        return "Excellent performance!"

    elif accuracy >= 60:
        return "Good job! Keep practicing."

    elif accuracy >= 40:
        return "You are improving. Keep trying!"

    else:
        return "Keep practicing and you will improve!"
