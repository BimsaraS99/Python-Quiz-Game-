import requests
import html

parameters = {
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean",
}
num_of_questions = 0


def get_question_data():

    try:
        response = requests.get("https://opentdb.com/api.php", params=parameters)
        all_questions = response.json()
    except:
        return False

    global num_of_questions
    question_data = list()
    for i in range(10):
        question = html.unescape(all_questions["results"][i]["question"])
        answer = all_questions["results"][i]["correct_answer"]
        question_data.append({"text": question, "answer": answer})

    num_of_questions = len(question_data)
    return question_data

