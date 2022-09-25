import random


class ManageQuiz:

    def __init__(self, question_list):
        self.question_list = question_list
        self.number_of_quiz = len(self.question_list)
        self.finished_quiz = []
        self.correct_quiz = 0
        self.wrong_quiz = 0

    def create_random_quiz(self):
        while True:
            quiz_number = random.randint(0, self.number_of_quiz-1)
            if not(quiz_number in self.finished_quiz):
                self.finished_quiz.append(quiz_number)
                return self.question_list[quiz_number]["text"], self.question_list[quiz_number]["answer"]

    def is_end_quiz(self):
        if self.number_of_quiz == len(self.finished_quiz):
            return True
        else:
            return False

    def internet_connected(self):
        if self.question_list[0]['answer'] == 'none':
            return False
        return True

    def quiz_number(self):
        return len(self.finished_quiz)

    def update_correct_answer(self):
        self.correct_quiz += 1

    def update_wrong_answer(self):
        self.wrong_quiz += 1
