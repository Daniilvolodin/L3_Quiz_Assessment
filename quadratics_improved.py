from tkinter import *


class Algebra_Entry:
    def __init__(self, parameter):
        self.parameter = parameter
        self.option_value = IntVar()

        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.question_label = Label(self.start_frame, text="-Label-",
                                    font="Arial 32 bold", padx=2, pady=1,
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
                                    command=lambda: self.get_value(), bg='green'
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


root = Tk()
app = Algebra_Entry(root)
root.title("Quadratics Practice")
root.mainloop()

