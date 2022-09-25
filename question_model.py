class Question:

    def __init__(self, quiz, ans):
        self.question = quiz
        self.answer = ans.lower()

    def is_answer_correct(self, answer):
        if answer == self.answer:
            return True
        else:
            return False

    def print_quiz(self):
        return self.question
