from tkinter import *
import random


def check_operator(x):
    if x >= 0:
        return "+" + str(x)
    else:
        return x


def change_colours(value, colour):
    str(colour)

    try:
        float(value)
    except ValueError:
        colour = '#eb5959'

        return colour

    else:
        colour = 'white'
        return colour


i_c = []
already_answered = []


def check_for_errors(value, message):
    str(message)

    try:
        float(value)
    except ValueError:
        if value.replace(' ', '') == '':
            message = 'No Blank'
        else:
            message = 'No Character'

        return message
    else:
        message = ''

        return message


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

        self.remaining_questions = Label(self.initialize_frame, text="Questions remaining {}".format(9 - len(i_c)),
                                         font="Arial 16 bold", fg='grey')
        self.remaining_questions.grid(row=2)

        self.entry_warning_label = Label(self.initialize_frame, fg='dark red')
        self.entry_warning_label.grid(row=3)

        if (9 - len(i_c)) < 0:
            self.initialize_frame.destroy()
            resultsShow()

    def on_submit(self):
        message = ''
        default = 'white'

        get_feedback = [self.get_variable1.get(), self.get_variable2.get()]
        for x in get_feedback:
            self.entry_warning_label.configure(text=check_for_errors(value=x, message=message))

        self.root_entry_1.configure(bg=change_colours(value=self.get_variable1.get(), colour=default))
        self.root_entry_2.configure(bg=change_colours(value=self.get_variable2.get(), colour=default))
        n1, n2 = self.get_variable1.get(), self.get_variable2.get()

        try:
            float(n1) and float(n2)
        except ValueError:
            pass
        else:
            attempt = [float(x) for x in [n1, n2]]
            correct = [-float(x) for x in [n1, n2]]
            attempt.sort(), correct.sort()
            if attempt == correct:
                print('Correct')
            self.initialize_frame.destroy()
            entryAlgebra(self)


class resultsShow:
    def __init__(self):
        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.correct_incorrect = Label(self.start_frame, text="Correct: {}\nIncorrect: {}".
                                       format(i_c.count("Correct"), i_c.count("Incorrect")),
                                       font="Arial 16 bold")
        self.correct_incorrect.grid(row=0)

        self.return_button = Button(self.start_frame, text="Return", font="Arial 16 bold",
                                    command=lambda: self.ret_to_quiz(), bg='grey')
        self.return_button.grid(row=1, sticky=NSEW)

    def ret_to_quiz(self):
        i_c.clear()
        self.start_frame.destroy()
        entryAlgebra(self)


if __name__ == "__main__":
    root = Tk()
    root.title("Questions about roots")
    root.geometry("270x270")
    app = entryAlgebra(root)
    root.mainloop()




