import tkinter as tk

from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz: QuizBrain) -> None:

        self.quiz = quiz
        self.score = 0
        self.window = tk.Tk()
        self.window.title("QuizMe")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.lbl_score = tk.Label(text=f"Score: {self.score}")
        self.lbl_score.config(background=THEME_COLOR, fg="white", font=("Courier", 12, "normal"))
        self.lbl_score.grid(column=1, row=0)

        self.canvas = tk.Canvas(self.window, bg="white", width=300, height=300)
        self.lbl_question = self.canvas.create_text(150, 125, text="", width=280, fill=THEME_COLOR,
                                                    font=("Courier", 20, "normal"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = tk.PhotoImage(file="images/true.png")
        self.btn_true = tk.Button(self.window, image=true_img, highlightthickness=0, command=self.true_pressed)
        self.btn_true.grid(column=0, row=2)

        false_img = tk.PhotoImage(file="images/false.png")
        self.btn_false = tk.Button(self.window, image=false_img, highlightthickness=0, command=self.false_pressed)
        self.btn_false.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def true_pressed(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
        else:
            q_text = "You have reached the end of the quiz"
            self.btn_false.config(state="disabled")
            self.btn_true.config(state="disabled")

        self.canvas.itemconfig(self.lbl_question, text=q_text)

    def give_feedback(self, is_right):
        if is_right:
            # let canvas turn green
            self.score += 1
            self.lbl_score.config(text=f"Score: {self.score}")
            self.canvas.config(bg="lightgreen")
            self.window.after(500, self.get_next_question)
        else:
            # let canvas turn red
            self.canvas.config(bg="orange red")
            self.window.after(500, self.get_next_question)
