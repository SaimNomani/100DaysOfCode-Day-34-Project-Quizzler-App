from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label=Label(text=f"Score: 0", fg='white', bg= THEME_COLOR, font=("Arial", 16, 'normal'))
        self.score_label.grid(row=0, column=1)

        self.canvas=Canvas(width=300, height=250, bg='white')
        self.canvas_text=self.canvas.create_text(150, 124,width=280, text="here is question text", fill='black',font=("Arial", 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_button_image=PhotoImage(file="images/true.png")
        wrong_button_image=PhotoImage(file="images/false.png")

        self.right_button=Button(image=right_button_image, highlightthickness=0, command=self.is_answer_correct)
        self.right_button.grid(row=2, column=0)

        self.wrong_button=Button(image=wrong_button_image, highlightthickness=0, command=self.is_answer_wrong)
        self.wrong_button.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()
    def get_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You have reched the end of quiz.")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
    def is_answer_correct(self):
        user_response= "true"
        print(user_response)
        self.feed_back(self.quiz.check_answer(user_response))
    def is_answer_wrong(self):
        user_response= "false"
        print(user_response)
        self.feed_back(self.quiz.check_answer(user_response))
    def feed_back(self, is_right):
        if is_right:
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.config( bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(2000, self.get_question)

