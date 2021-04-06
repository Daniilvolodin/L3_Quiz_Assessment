from tkinter import *
import random
import re


def check_operator(x):
    if x >= 0:
        return "+" + str(x)
    else:
        return x


class entryAlgebra:
    def __init__(self, parameter):

        acceptable = [random.randrange(-9, -1), random.randrange(1, 9)]
        random1, random2 = random.choice(acceptable), random.choice(acceptable)
        coef_pick = [1, 2, 3]
        x_coefficient1 = random.choice(coef_pick)
        x_coefficient2 = random.choice(coef_pick)
        show1 = check_operator(x=random1)
        show2 = check_operator(x=random2)
        question = "({}x{})({}x{})".format(x_coefficient1, show1, x_coefficient2, show2)

        self.correct_r_1, self.correct_r_2 = (-random1/x_coefficient1), -random2
        print(self.correct_r_1)
        print(self.correct_r_2)
        self.get_variable1 = StringVar()
        self.get_variable2 = StringVar()
        self.parameter = parameter
        self.initialize_frame = Frame()
        self.initialize_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.question_label = Label(self.initialize_frame, text=question, justify=CENTER,
                                    font="Arial 16 bold")
        self.question_label.grid(row=0, pady=10)

        self.entry_frame = Frame(self.initialize_frame)
        self.entry_frame.grid(row=1)

        self.label_root_1 = Label(self.entry_frame, text="First Root: ",
                                  font="Arial 10 bold")
        self.label_root_1.grid(row=1, column=0)

        self.root_entry_1 = Entry(self.entry_frame, width=6, textvariable=self.get_variable1)
        self.root_entry_1.grid(row=1, column=1)

        self.label_root_2 = Label(self.entry_frame, text="Second Root: ",
                                  font="Arial 10 bold")
        self.label_root_2.grid(row=2, column=0)

        self.root_entry_2 = Entry(self.entry_frame, width=6, textvariable=self.get_variable2)
        self.root_entry_2.grid(row=2, column=1, pady=5)

        self.submit_entry = Button(self.entry_frame, text='Submit', bg='#9597a3',
                                   font="Arial 12 bold", command=lambda: self.on_submit())
        self.submit_entry.grid(row=3, pady=5, sticky=NSEW, columnspan=2)

    def on_submit(self):

        variable1 = self.get_variable1.get().replace(" ", "")
        variable2 = self.get_variable2.get().replace(" ", "")
        var_pattern = '^[1-9][1-9]?/[1-9]?[1-9]$'
        check1 = re.match(var_pattern, variable1)

        if check1:
            n1 = int(variable1[0:1])
            print(n1)
            n2 = int(variable1[2])

        try:
            (float(variable1), float(variable2))

        except ValueError:
            print("No Character")

        else:
            if float(variable1) == round(self.correct_r_1, 2):
                print("Correct")


if __name__ == "__main__":
    root = Tk()
    root.title("Questions about roots")
    root.geometry("270x270")
    app = entryAlgebra(root)
    root.mainloop()
