# Add tkinter module
from tkinter import *
import random


# Operator checking function that decides what
# symbol to choose
def check_operator(x):
    if x >= 0:
        return "+" + str(x)
    else:
        return x


already_answered = []
i_c = []


# Class creates quiz window.
class Algebra_Entry:
    def __init__(self, parameter):
        # Initialise variables
        # Acceptable array prevents number zero from
        # appearing in question
        acceptable = [random.randrange(-9, -1), random.randrange(1, 9)]

        # Generates two integer variables from the range between -9,-1
        # and 1,9. One integer per variable
        random1, random2 = random.choice(acceptable), random.choice(acceptable)

        # Generates two co-efficients between 1,3
        coef_pick = [1, 2, 3]
        x_coefficient1 = random.choice(coef_pick)
        x_coefficient2 = random.choice(coef_pick)
        operators = ['+', '-']

        show1 = check_operator(x=random1)
        show2 = check_operator(x=random2)

        question = "({}x{})({}x{})".format(x_coefficient1, show1, x_coefficient2, show2)
        already_answered.append(question)

        # Operations to getting values from
        # complex form quadratic
        a_value = x_coefficient1 * x_coefficient2
        b_value = (x_coefficient1 * random2) + (x_coefficient2 * random1)
        c_value = random1 * random2

        # Variables use operate checking function to decide
        # whether the symbol is a plus or a minus
        b_op = check_operator(x=b_value)
        c_op = check_operator(x=c_value)
        alt_b_value = check_operator(x=b_value - (2 * (x_coefficient2 * random1)))

        # Number of questions in a quiz
        questions_left = 9

        # Creates alternative versions of options
        # one of four variables stores correct answers
        self.correct = "{}x²{}x{}".format(a_value, b_op, c_op)
        self.incorrect_1 = "{}x²{}x{}".format(a_value, str(b_op).replace(str(b_op)[0],
                                                                         operators[operators.index(str(b_op)[0]) - 1]),
                                              c_op)
        self.incorrect_2 = "{}x²{}x{}".format(a_value, b_op, check_operator(x=random1 + random2))
        self.incorrect_3 = "{}x²{}x{}".format(a_value, alt_b_value, c_op)

        self.answer_list = [self.correct, self.incorrect_1, self.incorrect_2, self.incorrect_3]
        random.shuffle(self.answer_list)

        self.parameter = parameter
        self.option_value = IntVar()

        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.question_label = Label(self.start_frame, text=question,
                                    font="Arial 24 bold", padx=2, pady=1,
                                    fg='grey')
        self.question_label.grid(row=0, sticky=N)

        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=1, sticky=N)

        self.option_1 = Radiobutton(self.button_frame, text="{}".format(self.answer_list[0]),
                                    variable=self.option_value, value=1, command=lambda: self.enable_submit_button()
                                    )
        self.option_1.grid(row=1, pady=3, sticky=NSEW)

        self.option_2 = Radiobutton(self.button_frame, text="{}".format(self.answer_list[1]),
                                    variable=self.option_value, value=2, command=lambda: self.enable_submit_button()
                                    )
        self.option_2.grid(row=2, pady=3, sticky=NSEW)

        self.option_3 = Radiobutton(self.button_frame, text="{}".format(self.answer_list[2]),
                                    variable=self.option_value, value=3, command=lambda: self.enable_submit_button()
                                    )
        self.option_3.grid(row=3, pady=3, sticky=NSEW)

        self.option_4 = Radiobutton(self.button_frame, text="{}".format(self.answer_list[3]),
                                    variable=self.option_value, value=4, command=lambda: self.enable_submit_button()
                                    )
        self.option_4.grid(row=4, pady=3, sticky=NSEW)

        self.submit_button = Button(self.button_frame, text="Submit", command=lambda: self.check_answer(),
                                    state=DISABLED)
        self.submit_button.grid(row=5, sticky=NSEW)

        self.remaining_label = Label(self.start_frame, text="Questions Remaining: {}"
                                     .format(questions_left - len(i_c)),
                                     fg='grey',
                                     font='Arial 16 bold')
        self.remaining_label.grid(row=2)

        # Checks the number of answers in a non-duplicate list
        # and compares it to the number of answers in original
        # list
        while len(set(already_answered)) != len(already_answered):
            print("Dupe")
            already_answered.remove(already_answered[-1])
            self.start_frame.destroy()
            Algebra_Entry(self)

        # Once the question variable hits its limit
        # It is going to call the score_win function
        # that directs user to his overall score
        if questions_left - len(i_c) < 0:
            self.to_score_win()
            i_c.clear()
            already_answered.clear()

    # Directs user to the score window
    def to_score_win(self):
        self.start_frame.destroy()
        statsWin()

    # Enables the submit button
    def enable_submit_button(self):
        self.submit_button.configure(state=NORMAL)

    # Function checks if user picked option is correct
    def check_answer(self):
        value = self.option_value.get()
        user_answer = self.answer_list[value - 1]

        # Checks if option is correct or incorrect and adds
        # user answer to a list
        if user_answer is self.correct:
            i_c.append("Correct")
        else:
            i_c.append("Incorrect")

        self.start_frame.destroy()
        Algebra_Entry(self)


# Creates a stats window which shows
# User score
class statsWin:
    def __init__(self):
        self.show_win = Frame()
        self.show_win.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.score_label = Label(self.show_win, padx=10, pady=10, fg='grey',
                                 text="Incorrect: {}\nCorrect: {}"
                                 .format(i_c.count("Incorrect"),
                                         i_c.count("Correct")),
                                 font="Arial 10 bold")
        self.score_label.grid(row=0)

        self.return_button = Button(self.show_win, padx=3, pady=2,
                                    font='Arial 16 bold', bg='grey',
                                    text='Return', command=lambda: self.main_gui_return())
        self.return_button.grid(row=1)

    def main_gui_return(self):
        self.show_win.destroy()
        Algebra_Entry(self)


# Initialise GUI window
root = Tk()
app = Algebra_Entry(root)
root.geometry("270x270")
root.title("Quadratics Practice")
root.mainloop()



