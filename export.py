from tkinter import *
import re

# No symbols
# No blank spaces
# No spaces
# list for storing the number of times
# user entered incorrect/correct value
data = []
# number of times user pressed incorrect
incorrect = []
# number of times user pressed correct
correct = []


# Main window for export class
class export:
    def __init__(self, parameter):
        self.parameter = parameter

        self.mainFrame = Frame()
        self.mainFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.button_frame = Frame(self.mainFrame)
        self.button_frame.grid(row=0)
        # Button responsible for registering incorrect input
        self.button_incorrect = Button(self.button_frame, text='Incorrect', font='Arial 16 bold',
                                       command=lambda: self.incorrect_1(), fg='white', bg='grey')
        self.button_incorrect.grid(row=0, column=0)
        # Button responsible for registering correct input
        self.button_correct = Button(self.button_frame, text='Correct', font='Arial 16 bold',
                                     command=lambda: self.correct_1(), fg='white', bg='grey')
        self.button_correct.grid(row=0, column=1)

        # Directs user to export window
        self.export_button = Button(self.mainFrame, text='Export', font='Arial 16 italic',
                                    command=lambda: self.to_stat())
        self.export_button.grid(row=1, sticky=NSEW)

        self.label_correct = Label(self.mainFrame, text="Correct: {}".format(len(correct)))
        self.label_correct.grid(row=2)

        self.label_incorrect = Label(self.mainFrame, text="Incorrect: {}".format(len(incorrect)))
        self.label_incorrect.grid(row=3)

    # Adds a string to data and correct list
    def correct_1(self):
        data.append('Correct')
        correct.append('Correct')
        # Refreshes correct label
        self.label_correct.configure(text="Correct: {}".format(len(correct)))

    # Adds a string to data and incorrect list
    def incorrect_1(self):
        data.append('Incorrect')
        incorrect.append('Incorrect')
        # Refreshes incorrect label
        self.label_incorrect.configure(text="Incorrect: {}".format(len(incorrect)))

    # Directs user to export screen
    def to_stat(self):
        self.mainFrame.destroy()
        export_stat()


class export_stat:
    def __init__(self):
        self.new_frame = Frame()
        # allows the input to have capital letters and digits
        self.valid_char = r'[A-Za-z1-9]'

        self.new_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.both = Frame(self.new_frame)
        self.both.grid(row=0)
        self.entry = Entry(self.both, font='helvetica 12 italic',
                           justify=CENTER)
        self.entry.grid(row=0)
        # submits user input and checks whether it's valid or not
        self.button = Button(self.both, text='SUBMIT', font='Arial 13 bold',
                             bg='grey', fg='white', command=lambda: self.check_regex())
        self.button.grid(row=1, sticky=NSEW, pady=(10, 0))

        self.warning_label = Label(self.new_frame, font='Arial 16 italic', fg='red')
        self.warning_label.grid(row=1)

    def check_regex(self):
        check = self.entry.get()

        problem = ''
        for v in check:
            # if input is valid, the program continues
            if re.match(r'[A-Za-z1-9]', v):
                continue
            # if input is empty, the message will
            # be set to warn user that it cannot contain
            # blank spaces
            if v == '':
                problem = 'No blank spaces'
            # Cannot contain symbols
            else:
                problem = 'No Symbols Such As ' + str(v)
            break

        # File name cannot be left blank
        if len(data) == 0:
            problem = 'Cannot be an empty file'
        if check == '':
            problem = 'Cannot be blank'
        # show warning message if there is a problem
        if problem != '':
            self.warning_label.configure(text=problem)
            return
        # otherwise, the program creates a text file
        # with user results
        else:
            self.warning_label.configure(text='Clear', fg='green')
            filename = str(self.entry.get())+'.txt'
            f = open(filename, 'w+')
            for x in data:
                f.write(str(x) + '\n')
            f.read()
            f.close()
            self.new_frame.destroy()
            export(self)


root = Tk()
root.geometry("360x380")
app = export(root)
root.mainloop()

