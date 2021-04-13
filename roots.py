from tkinter import *
import random


# Function that decides whether to put a plus
# or a minus
def check_operator(x):
    if x >= 0:
        return "+" + str(x)
    else:
        return x


# Function checks if user input is a number
# if it's valid, the colour is white
# if it's not valid, the colour is pale red
def change_colours(value, colour):
    str(colour)
    stripped = value.replace(' ', '')
    try:
        float(stripped)
    except ValueError:
        colour = '#eb5959'

        return colour

    else:
        colour = 'white'
        return colour


# List for counting correct/incorrect answers
i_c = []
# List for taking in user answered questions
already_answered = []


# Function checks if user input is a number
# If input is a number, warning message will be blank
# If input is a blank, warning message will say
# the input cannot be empty
# If input is a character, warning message will say
# the input cannot contain characters
def check_for_errors(value, message):
    str(message)

    try:
        float(value.replace(' ', ''))

    except ValueError:

        if value.replace(' ', '') == '':
            message = 'Cannot be blank'
        else:
            message = 'Cannot contain characters'

        return message
    else:

        pass


# Starting UI
# Contains all the buttons and entries
# Contains variables that use random library
# random integers are being generated within this class
class entryAlgebra:
    def __init__(self, parameter):
        # Recycled variables from the previous component
        acceptable1 = [random.randrange(-9, -1), random.randrange(1, 9)]
        acceptable2 = [random.randrange(-9, -1), random.randrange(1, 9)]

        random1, random2 = random.choice(acceptable1), random.choice(acceptable2)

        # Check op function is incremented in random gen numbers
        self.show1 = check_operator(x=random1)
        self.show2 = check_operator(x=random2)

        question = "(x{})(x{})".format(self.show1, self.show2)
        self.question_check = question

        questions_duped = False

        # Initializes two string variables
        self.get_variable1 = StringVar()
        self.get_variable2 = StringVar()

        self.parameter = parameter

        # Starting frame contains every widget
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

        # Recycled from previous component
        # checks if there was a duplicate answer
        for x in range(len(already_answered)):
            if self.question_check in already_answered:
                questions_duped = True
        if questions_duped is not False:
            print("There was a duplicate answer")
            self.initialize_frame.destroy()
            entryAlgebra(self)

        if (9 - len(i_c)) < 0:
            self.initialize_frame.destroy()
            resultsShow()

    def on_submit(self):
        message = ''
        default = 'white'

        get_feedback = [self.get_variable1.get(), self.get_variable2.get()]
        # Goes through user input to find a discrepancy
        for x in get_feedback:
            # Generates appropriate message based on user input

            self.entry_warning_label.configure(text=check_for_errors(value=x, message=message))

        # Sets user entry background colour base on his input
        self.root_entry_1.configure(bg=change_colours(value=self.get_variable1.get(), colour=default))
        self.root_entry_2.configure(bg=change_colours(value=self.get_variable2.get(), colour=default))
        n1, n2 = self.get_variable1.get().replace(' ', ''), self.get_variable2.get().replace(' ', '')

        # turns user input into integer form
        try:
            float(n1) and float(n2)
        # if user integer form is invalid
        # the program keeps user on the
        # same question until he fills it in correctly
        except ValueError:
            print("ERROR")
            pass

        else:
            # Sets every value to a number
            attempt = [float(x) for x in [n1, n2]]
            correct = [-float(x) for x in [self.show1, self.show2]]
            attempt.sort(), correct.sort()

            if attempt == correct:
                i_c.append("Correct")
                print("Correct")
            else:
                i_c.append("Incorrect")
                print("Incorrect")
            already_answered.append(self.question_check)
            self.initialize_frame.destroy()
            entryAlgebra(self)


# Results UI appears after use completed the quiz
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

    # Returns user back to starting UI
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



