from tkinter import *
import random


class Quadratics_Entry:
    def __init__(self):
        self.random_1, self.random_2 = random.randrange(1, 10), random.randint(1, 6)
        self.symbols = ["+", "-"]
        self.symbol_random_1, self.symbol_random_2 = random.choice(self.symbols), random.choice(self.symbols)

        self.remaining_symbol_1 = self.symbols.index(self.symbol_random_1)
        self.counter_1 = self.symbols[self.remaining_symbol_1 - 1]

        self.remaining_symbol_2 = self.symbols.index(self.symbol_random_2)
        self.counter_2 = self.symbols[self.remaining_symbol_2 - 1]

        self.x_coefficient_1 = [1, 2, 3]
        self.coefficient_random_1 = random.randint(1, len(self.x_coefficient_1) - 1)

        self.x_coefficient_2 = [1, 2, 3]
        self.coefficient_random_2 = random.randint(0, len(self.x_coefficient_1) - 1)

        self.correct_answer = [self.counter_1+str(self.random_1), self.counter_2+str(self.random_2)]
        self.incorrect_1 = [str(self.random_1), str(self.random_2)]
        self.incorrect_2 = [str(self.random_1), str(self.random_2)]
        self.incorrect_3 = [str(self.random_1), str(self.random_2)]

        print(self.correct_answer)


inter_variable = Quadratics_Entry()

gather_quadratics = [inter_variable.random_1, inter_variable.random_2, inter_variable.symbols,
                     inter_variable.symbol_random_1, inter_variable.symbol_random_2,
                     inter_variable.x_coefficient_1, inter_variable.coefficient_random_1,
                     inter_variable.x_coefficient_2, inter_variable.coefficient_random_2]


class Algebra_Entry:
    def __init__(self, parameter):
        self.parameter = parameter

        self.option_value = IntVar()

        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.main_frame = Frame(self.start_frame, pady=10, bg='black', padx=10)
        self.main_frame.grid(row=0)

        self.question_label = Label(self.main_frame, padx=10, pady=10,
                                    text="({}x{}{})({}x{}{})".format(
                                        inter_variable.x_coefficient_1[inter_variable.coefficient_random_1],
                                        inter_variable.symbol_random_1,
                                        inter_variable.random_1,
                                        inter_variable.x_coefficient_2[inter_variable.coefficient_random_2],
                                        inter_variable.symbol_random_2,
                                        inter_variable.random_2), font="Arial 32 bold")
        self.question_label.grid(row=0)

        self.option_1 = Radiobutton(self.main_frame, text="Option 1",
                                    value=1, variable=self.option_value
                                    )
        self.option_1.grid(row=1, pady=3, sticky=NSEW)

        self.option_2 = Radiobutton(self.main_frame, text="Option 2",
                                    value=2, variable=self.option_value
                                    )
        self.option_2.grid(row=2, pady=3, sticky=NSEW)

        self.option_3 = Radiobutton(self.main_frame, text="Option 3",
                                    value=3, variable=self.option_value
                                    )
        self.option_3.grid(row=3, pady=3, sticky=NSEW)

        self.option_4 = Radiobutton(self.main_frame, text="Option 4",
                                    value=4, variable=self.option_value
                                    )
        self.option_4.grid(row=4, pady=3, sticky=NSEW)

        self.submit_button = Button(self.main_frame, text="Submit",
                                    command=lambda: self.check_answer())
        self.submit_button.grid(row=5, pady=3, sticky=NSEW)

    def check_answer(self):
        self.start_frame.destroy()


root = Tk()
root.geometry("500x500")
app = Algebra_Entry(root)
root.mainloop()
