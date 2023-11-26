import random
import html
import requests


question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.",
     "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.",
     "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.",
     "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.",
     "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.",
        "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.",
     "answer": "True"}
]


class DataBase:
    def __init__(self, difficulty='', num=100) -> None:
        self.q_diff = difficulty
        self.q_amonut = num

    def get_new_questions(self):
        """collect new questions from an API

        ### Returns:
            list: list of questions recieved from api
        """
        question_db = question_data.copy()
        response = requests.get(
            f"https://opentdb.com/api.php?amount={self.q_amonut}&type=boolean&difficulty=" + self.q_diff, timeout=10)
        print(response.status_code)
        if response.status_code == 200:
            results = response.json()['results']
            for a_q in results:
                question = html.unescape(a_q['question'])
                question_db.append({"text": question, "answer": a_q['correct_answer']})

            random.shuffle(question_db)
        else:
            print(f"DataBase creation failure with error code : "
                  f"{response.status_code}")
        return question_db
