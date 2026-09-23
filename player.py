class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.questions_answered = 0
        self.correct_answers = 0

    def add_score(self, points):
        self.score += points

    def record_answer(self, correct):
        self.questions_answered += 1

        if correct:
            self.correct_answers += 1

    def get_accuracy(self):
        if self.questions_answered == 0:
            return 0

        return (self.correct_answers / self.questions_answered) * 100
