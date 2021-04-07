from tkinter import *
import random


def check_operator(x):
    if x >= 0:
        return "+" + str(x)
    else:
        return x

i_c = []
already_answered = []


class entryAlgebra:
    def __init__(self, parameter):

        acceptable1 = [random.randrange(-9, -1), random.randrange(1, 9)]
        acceptable2 = [random.randrange(-9, -1), random.randrange(1, 9)]
        random1, random2 = random.choice(acceptable1), random.choice(acceptable2)
        self.show1 = check_operator(x=random1)
        self.show2 = check_operator(x=random2)
        question = "(x{})(x{})".format(self.show1, self.show2)

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
        try:
            two_of = [int(self.get_variable1.get()),
                      int(self.get_variable2.get())]
            two_of.sort()

            correct = [-1*int(self.show1), -1*int(self.show2)]
            correct.sort()

        except ValueError:
            print("Cannot be a character or a symbol")

        else:
            if two_of == correct:
                i_c.append('Correct')
            else:
                i_c.append('Incorrect')
            print(i_c)
            self.initialize_frame.destroy()
            entryAlgebra(self)

if __name__ == "__main__":
    root = Tk()
    root.title("Questions about roots")
    root.geometry("270x270")
    app = entryAlgebra(root)
    root.mainloop()

