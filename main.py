""" contains main workflow of the quiz game
    """
from question_model import Question
from data import DataBase
from quiz_brain import QuizBrain
from ui import QuizUI


def main():
    """ main overflow
    """
    question_bank = []
    db = DataBase(num=50)
    questions = db.get_new_questions()
    for qu in questions:
        question_bank.append(Question(qu["text"], qu["answer"]))

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizUI(quiz)


if __name__ == "__main__":
    main()
