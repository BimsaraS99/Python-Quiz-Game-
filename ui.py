from tkinter import *
import manage_quiz
import question_model

THEME_COLOR = "#375362"
NO_INTERNET = [{'text': 'Check your internet connection !!!.', 'answer': 'none'}]


class QuizInterface:

    def __init__(self, questions=NO_INTERNET):
        self.manage_questions = manage_quiz.ManageQuiz(questions)
        self.quiz_object = None  # this variable store the current question as an object
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.resizable(False, False)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.buttons_state = True  # if this is True, button inputs are valid. But if False button inputs are ignored

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 15))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Wait", fill=THEME_COLOR,
                                                     font=("Arial", 17, "italic"), width=280)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.click_true)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.click_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if not self.manage_questions.is_end_quiz():
            if self.manage_questions.internet_connected():
                self.buttons_state = True
                self.canvas.config(bg='white')
                question_text, answer = self.manage_questions.create_random_quiz()
                print(question_text, answer)
                self.quiz_object = question_model.Question(question_text, answer)
                text = f"Q{self.manage_questions.quiz_number()}: {self.quiz_object.print_quiz()}"
                self.canvas.itemconfig(self.question_text, text=text)
            else:
                self.display_no_internet()
        else:
            self.end_screen()

    def process_answer(self, user_answer):
        self.buttons_state = False
        if user_answer:
            self.canvas.config(bg='#77E675')
            self.manage_questions.update_correct_answer()
            self.score_label.config(text=f"Score: {self.manage_questions.correct_quiz}")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg='#E67575')
            self.manage_questions.update_wrong_answer()
            self.score_label.config(text=f"Score: {self.manage_questions.correct_quiz}")
            self.window.after(1000, self.get_next_question)

    def click_true(self):
        if self.manage_questions.internet_connected() and self.buttons_state:
            answer = self.quiz_object.is_answer_correct('true')
            self.process_answer(answer)

    def click_false(self):
        if self.manage_questions.internet_connected() and self.buttons_state:
            answer = self.quiz_object.is_answer_correct('false')
            self.process_answer(answer)

    def end_screen(self):
        self.canvas.config(bg='#8599E9')
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        text = f"Your Final Score:\n          " \
               f"{self.manage_questions.correct_quiz} / {self.manage_questions.number_of_quiz}"
        self.canvas.itemconfig(self.question_text, text=text)

    def display_no_internet(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.canvas.config(bg='#8D8E92')
        self.canvas.itemconfig(self.question_text, text="No Internet")
