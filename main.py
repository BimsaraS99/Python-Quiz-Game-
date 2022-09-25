import data
import ui

questions = data.get_question_data()
if questions:
    gui = ui.QuizInterface(questions)
else:
    gui = ui.QuizInterface()
