from tkinter import *
from functools import partial
import random


# Function that decides whether to put a plus
# or a minus
def check_operator(x):
    if int(x) >= 0:
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


# Regular expression function
# Checks if user input looks like a
# quadratic equation, if not the
# entry field turns red
def regex_check(value):
    check_answer = re.match(r'^\(x[+\-]\d*\)\(x[+\-]\d*\)$', value.get())
    if check_answer:
        return value.configure(bg='white')
    else:
        return value.configure(bg='#eb5959')


class rectangle:
    def __init__(self, parameter):
        self.parameter = parameter
        # Recycled variables from the previous component
        acceptable = [random.randrange(-9, -1), random.randrange(1, 9)]
        self.ran1, self.ran2 = check_operator(x=random.choice(acceptable)), check_operator(x=random.choice(acceptable))

        # Forms a quadratic equation
        self.question = "x²{}x{}".format(check_operator(x=(int(self.ran1) + int(self.ran2))),
                                         check_operator(x=(int(self.ran1) * int(self.ran2))))
        # Text variable that is used within quadratic entry
        self.string_set = StringVar()

        # Frame containing all the contents
        self.frame_one = Frame()
        self.frame_one.grid(padx=30, pady=30)
        # Text variables that are use in height and width entries
        self.string_height = StringVar()
        self.string_width = StringVar()

        # Label contains a question asking to find a simplified quadratic
        # and two of its roots
        self.label = Label(self.frame_one,
                           text="The area of a rectangle can be represented by: {}.\n"
                                "Find simplified quadratic form and define its roots".format(self.question),
                           wrap=200)
        self.label.grid(row=0)

        self.simplified = Entry(self.frame_one, justify=CENTER, relief=FLAT, highlightbackground='black',
                                highlightthickness=1, textvariable=self.string_set)
        self.simplified.grid(row=1, sticky=NSEW)

        self.buttons = Frame(self.frame_one)
        self.buttons.grid(row=2, sticky=NSEW, pady=(5, 0))
        # Checks if user quadratic is valid / invokes on_check function
        self.check_button = Button(self.buttons, text="CHECK", bg="grey", fg="white",
                                   font="Arial 12 bold", width=16, relief=FLAT,
                                   command=lambda: self.on_check())
        self.check_button.grid(row=2, column=0, padx=(0, 5), sticky=NSEW, pady=(5, 0))
        # Creates new window with relevant information about sim. quadratic
        # entry.
        self.help_button = Button(self.buttons, text="?", bg="grey", fg="white",
                                  font="Arial 12 bold", relief=FLAT, command=lambda: self.on_help())
        self.help_button.grid(row=2, column=1, sticky=NSEW, pady=(5, 0))

        self.width_label = Label(self.buttons, text="Width:")
        self.width_label.grid(row=3, column=0, pady=(10, 0))

        self.width_entry = Entry(self.buttons, width=4, justify=CENTER, relief=FLAT, highlightbackground='black',
                                 highlightthickness=1, textvariable=self.string_width)
        self.width_entry.grid(row=3, column=1, sticky=NSEW, pady=(10, 0))

        self.height_label = Label(self.buttons, text="Height:")
        self.height_label.grid(row=4, column=0, pady=(10, 0))

        self.height_entry = Entry(self.buttons, width=4, justify=CENTER, relief=FLAT, highlightbackground='black',
                                  highlightthickness=1, textvariable=self.string_height)
        self.height_entry.grid(row=4, column=1, sticky=NSEW, pady=(10, 0))
        # Checks if all entry fields are correctly filled in by using on_submit function
        self.submit_button = Button(self.frame_one, text="SUBMIT",
                                    font="Arial 12 bold", fg='white', bg='grey',
                                    relief=FLAT, command=lambda: self.on_submit())
        self.submit_button.grid(row=3, sticky=NSEW, pady=(10, 0))

        self.warning_message = Label(self.frame_one, text="", fg='red')
        self.warning_message.grid(row=4, sticky=NSEW, pady=(10, 0))

    def on_submit(self):
        # List containing width / height input
        attempted = [self.width_entry.get(), self.height_entry.get()]
        message = None

        # Goes through width / height input to find
        # discrepancies using check_for_errors function
        # Displays warning message if there are errors
        for x in attempted:
            self.warning_message.configure(text=check_for_errors(value=x, message=message))

        # Changes entry background colour based on user input
        # If there is an error, the entry will be displayed with red colour
        # otherwise, the default colour is white
        self.height_entry.configure(bg=change_colours(value=self.string_height.get(), colour='white'))
        self.width_entry.configure(bg=change_colours(value=self.string_width.get(), colour='white'))
        regex_check(value=self.simplified)

        # Removes all blank spaces in  width / height input
        num1, num2 = self.string_height.get().replace(' ', ''), self.string_width.get().replace(' ', '')

        # Converts user string input into a number
        # with decimal places.
        try:
            float(num1) and float(num2)

        # If user input is not an integer
        # The program will not progress until
        # it receives a valid input
        except ValueError:
            pass
        else:
            self.warning_message.configure(text='')
            # Regular Expression: If user input doesn't meet the
            # simplified quadratic criteria, the program will not
            # continue until it does.
            if not re.match(r'^\(x[+\-]\d*\)\(x[+\-]\d*\)$', self.simplified.get()):
                return
            # Turns every user input into a float integer
            attempt = [float(x) for x in [num1, num2]]
            # Turns ran. gen. number into a float and multiplies
            # it by negative one
            correct = [-float(v) for v in [self.ran1, self.ran2]]
            # Sorting number in an order from highest to lowest
            attempt.sort(), correct.sort()
            # Stores correct simplified quadratic answer
            correct_answer = ["(x{})(x{})".format(self.ran1, self.ran2),
                              "(x{})(x{})".format(self.ran2, self.ran1)]
            # If user gets height and width input
            # correct, program prints "Correct"
            if attempt == correct:
                print("Correct")
            # Same for simplified quadratic input
            if self.simplified.get() in correct_answer:
                print("Correctness")

            # Refreshes question about rectangle
            self.frame_one.destroy()
            rectangle(self)

    # Checks if user quadratic meets criteria
    # of valid input
    def on_check(self):
        regex_check(value=self.simplified)

    # Launches a help window
    def on_help(self):
        helpWin(self)


class helpWin:
    def __init__(self, parameter):
        parameter.help_button.config(state=DISABLED)
        # New Window (Help window)
        self.newFrame = Toplevel()
        self.newFrame.geometry("300x300")
        self.newFrame.grid()
        # Prevents from creating multiple of Help windows
        self.newFrame.protocol("WM_DELETE_WINDOW", partial(self.leave, parameter))

        # Contains Help window content
        self.content_frame = Frame(self.newFrame)
        self.content_frame.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.index_frame = Frame(self.content_frame)
        self.index_frame.grid(row=0)
        # Label includes instruction of what is required
        # of user for a program to validate his answer
        self.title = Label(self.index_frame, text="Help Index", font="Arial 20 bold")
        self.title.grid(row=0, pady=(0, 10))

        self.contents = Label(self.index_frame, text="Entry Requirements",
                              font="Arial 10 bold")
        self.contents.grid(row=1)

        self.instructions = Label(self.index_frame, text="Enter your input in a form of "
                                                         "simplified quadratic equation\n\n"
                                                         "When using exemplars, change "
                                                         "hash tags to a number for "
                                                         "program to validate your input.",
                                  font="Arial 10 italic", wrap=180, justify=LEFT)
        self.instructions.grid(row=2)

        self.button_frame = Frame(self.newFrame)
        self.button_frame.place(relx=0.5, rely=0.9, anchor=CENTER)

        # Closes Help window
        self.dismiss_button = Button(self.button_frame, text="Dismiss",
                                     command=partial(self.leave, parameter), bg='grey', fg='white',
                                     font='Arial 12 bold', relief=FLAT)
        self.dismiss_button.grid(row=0, column=0, padx=(0, 5), pady=10)

        # Forms quadratic equation based on exemplar
        # by replacing hash tags with integer to
        # prevent unwanted correct answers
        self.form_quad = Button(self.button_frame, text="Set Exemplar",
                                command=lambda: self.form_quad_eq(parameter), relief=FLAT,
                                bg='grey', fg='white', font="Arial 12 bold")
        self.form_quad.grid(row=0, column=1)
        # If exemplar is already present, the
        # button becomes disabled
        if parameter.string_set.get() == "(x+#)(x+#)":
            self.form_quad.configure(state=DISABLED)

    # Sets 'simplified' entry to exemplar and
    # disables form exemplar button
    def form_quad_eq(self, parameter):
        parameter.string_set.set("(x+#)(x+#)")
        self.form_quad.configure(state=DISABLED)

    # Exits Help window
    def leave(self, parameter):
        self.newFrame.destroy()

        parameter.help_button.config(state=NORMAL)


root = Tk()
root.title("Rectangle Questions")
app = rectangle(root)
root.mainloop()


