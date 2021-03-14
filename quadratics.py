from tkinter import *
import random

random_1, random_2 = random.randrange(1, 10), random.randint(1, 10)

symbols = ["+", "-"]

symbol_random_1, symbol_random_2 = random.choice(symbols), random.choice(symbols)

x_coefficient_1 = ['', 2, 3]
coefficient_random_1 = random.randint(1, len(x_coefficient_1) - 1)

x_coefficient_2 = ['', 2, 3]
coefficient_random_2 = random.randint(0, len(x_coefficient_1) - 1)

gather_quadratics = [random_1, random_2, symbols,
                     symbol_random_1, symbol_random_2,
                     x_coefficient_1, coefficient_random_1,
                     x_coefficient_2, coefficient_random_2]

correct = "{}/{}".format(random_1, x_coefficient_1[coefficient_random_1])
incorrect = {}
for i in range(4):
    incorrect[i] = "{}/{}".format(random_1, x_coefficient_1[coefficient_random_1])

print(incorrect)


class algebra:
    def __init__(self, parameter):
        self.option_value = IntVar()

        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.main_frame = Frame(self.start_frame, pady=10, bg='black', padx=10)
        self.main_frame.grid(row=0)

        self.question_label = Label(self.main_frame, padx=10, pady=10,
                                    text="({}x{}{})({}x{}{})".format(x_coefficient_1[coefficient_random_1],
                                                                     symbol_random_1,
                                                                     random_1, x_coefficient_2[coefficient_random_2],
                                                                     symbol_random_2,
                                                                     random_2), font="Arial 32 bold")
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
                                    command=lambda: self.check_answer(self.option_value.get()))
        self.submit_button.grid(row=5, pady=3, sticky=NSEW)

    def check_answer(self, value):
        self.start_frame.destroy()


root = Tk()
root.geometry("500x500")
app = algebra(root)
root.mainloop()
