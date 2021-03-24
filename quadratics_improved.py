# Add tkinter module
from tkinter import *
import random

already_answered = []


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
        show1, show2 = random1, random2

        if random1 >= 0:
            show1 = "+" + str(random1)
        if random2 >= 0:
            show2 = "+" + str(random2)

        question = "({}x{})({}x{})".format(x_coefficient1, show1, x_coefficient2, show2)

        a_value = x_coefficient1 * x_coefficient2
        b_value = (x_coefficient1 * random2) + (x_coefficient2 * random1)
        c_value = random1 * random2
        b_op = b_value
        c_op = c_value

        if b_value >= 0:
            b_op = "+" + str(b_value)
        if c_value >= 0:
            c_op = "+" + str(c_value)

        answer_dict = {
            "Correct": "{}x²{}x{}".format(a_value, b_op, c_op),
            "Incorrect1": "{}x²{}x{}".format(a_value, str(b_op).replace(str(b_op)[0],
                                             str(operators[operators.index(str(b_op)[0])-1])), c_op),

            "Incorrect2": "{}x²{}x{}".format(a_value, b_op, random1 + random2),
            "Incorrect3": "{}x²{}x{}".format(a_value, int(b_op)+random2, c_op)
        }
        print(int(b_op)+random2)
        print(answer_dict.get("Incorrect1"))
        print(answer_dict.get("Incorrect2"))
        print(answer_dict.get("Incorrect3"))
        print(answer_dict.get("Correct"))
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

        self.option_1 = Radiobutton(self.button_frame, text="{1}",
                                    variable=self.option_value, value=1,
                                    command=lambda: self.get_value()
                                    )
        self.option_1.grid(row=1, pady=3, sticky=NSEW)

        self.option_2 = Radiobutton(self.button_frame, text="{2}",
                                    variable=self.option_value, value=2,
                                    command=lambda: self.get_value()
                                    )
        self.option_2.grid(row=2, pady=3, sticky=NSEW)

        self.option_3 = Radiobutton(self.button_frame, text="{3}",
                                    variable=self.option_value, value=3,
                                    command=lambda: self.get_value(), anchor=CENTER
                                    )
        self.option_3.grid(row=3, pady=3, sticky=NSEW)

        self.option_4 = Radiobutton(self.button_frame, text="{4}",
                                    variable=self.option_value, value=4,
                                    command=lambda: self.get_value()
                                    )
        self.option_4.grid(row=4, pady=3, sticky=NSEW)

        self.submit_button = Button(self.button_frame, text="Submit")
        self.submit_button.grid(row=5, sticky=NSEW)

    def get_value(self):
        q = self.option_value.get()
        print(q)


# Initialise GUI window
root = Tk()
app = Algebra_Entry(root)
root.title("Quadratics Practice")
root.mainloop()


