"""quiz_brain
    """


import time
from question_model import Question


class QuizBrain:
    """responsible for running all quiz actions
    """

    def __init__(self, question_bank):
        self.q_number = 0
        self.next_q = Question("", "False")
        self.q_list = question_bank

    def next_question(self):
        """print next question to user and catch his answer
        """
        self.next_q = self.q_list[self.q_number]
        self.q_number += 1
        the_question = f"Q.{self.q_number}: {self.next_q.text}"
        return the_question

    def check_answer(self, usr_answer):
        """check if user answer correctly

        ### Parameters:
            usr_answer (str): the answer the user inputed
            correct_answer (str): either a value of 'True' or 'False'
        """
        correct_answer = self.next_q.answer
        if usr_answer == correct_answer:
            return True
        else:
            return False

    def still_has_questions(self):
        """check if the question list still have unaslked questions

        ### Returns:
            bool: True if there is still unasked question , False otherwise
        """
        return len(self.q_list) > self.q_number
