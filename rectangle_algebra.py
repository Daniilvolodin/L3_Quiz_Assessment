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


def regex_check(value):
    check_answer = re.match(r'^\(x[+\-]\d*\)\(x[+\-]\d*\)$', value.get())
    if check_answer:
        return value.configure(bg='white')
    else:
        return value.configure(bg='#eb5959')


class rectangle:
    def __init__(self, parameter):
        self.parameter = parameter
        acceptable = [random.randrange(-9, -1), random.randrange(1, 9)]
        self.ran1, self.ran2 = check_operator(x=random.choice(acceptable)), check_operator(x=random.choice(acceptable))

        self.question = "x²{}x{}".format(check_operator(x=(int(self.ran1) + int(self.ran2))),
                                         check_operator(x=(int(self.ran1) * int(self.ran2))))

        self.string_set = StringVar()
        self.frame_one = Frame()
        self.frame_one.grid(padx=80, pady=80)

        self.string_height = StringVar()
        self.string_width = StringVar()

        self.label = Label(self.frame_one,
                           text="The area of a rectangle can be represented by: {}".format(self.question),
                           wrap=200)
        self.label.grid(row=0)

        self.simplified = Entry(self.frame_one, justify=CENTER, relief=FLAT, highlightbackground='black',
                                highlightthickness=1, textvariable=self.string_set)
        self.simplified.grid(row=1, sticky=NSEW)

        self.buttons = Frame(self.frame_one)
        self.buttons.grid(row=2, sticky=NSEW, pady=(5, 0))

        self.check_button = Button(self.buttons, text="CHECK", bg="grey", fg="white",
                                   font="Arial 12 bold", width=16, relief=FLAT,
                                   command=lambda: self.on_check())
        self.check_button.grid(row=2, column=0, padx=(0, 5), sticky=NSEW, pady=(5, 0))

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

        self.submit_button = Button(self.frame_one, text="SUBMIT",
                                    font="Arial 12 bold", fg='white', bg='grey',
                                    relief=FLAT, command=lambda: self.on_submit())
        self.submit_button.grid(row=3, sticky=NSEW, pady=(10, 0))

        self.warning_message = Label(self.frame_one, text="", fg='red')
        self.warning_message.grid(row=4, sticky=NSEW, pady=(10, 0))

    def on_submit(self):
        attempted = [self.width_entry.get(), self.height_entry.get()]
        message = ''

        for x in attempted:
            self.warning_message.configure(text=check_for_errors(value=x, message=message))

        self.height_entry.configure(bg=change_colours(value=self.string_height.get(), colour='white'))
        self.width_entry.configure(bg=change_colours(value=self.string_width.get(), colour='white'))
        regex_check(value=self.simplified)
        num1, num2 = self.string_height.get().replace(' ', ''), self.string_width.get().replace(' ', '')

        try:
            float(num1) and float(num2)
        except ValueError:
            pass
        else:
            self.warning_message.configure(text='')
            attempt = [float(x) for x in [num1, num2]]
            correct = [-float(v) for v in [self.ran1, self.ran2]]
            attempt.sort(), correct.sort()
            correct_answer = ["(x{})(x{})".format(self.ran1, self.ran2),
                              "(x{})(x{})".format(self.ran2, self.ran1)]
            if attempt == correct:
                print("Correct")
            if self.simplified.get() in correct_answer:
                print("Correctness")

    def on_check(self):
        regex_check(value=self.simplified)

    def on_help(self):
        helpWin(self)


class helpWin:
    def __init__(self, parameter):

        parameter.help_button.config(state=DISABLED)

        self.newFrame = Toplevel()
        self.newFrame.geometry("300x300")
        self.newFrame.grid()
        self.newFrame.protocol("WM_DELETE_WINDOW", partial(self.leave, parameter))

        self.content_frame = Frame(self.newFrame)
        self.content_frame.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.index_frame = Frame(self.content_frame)
        self.index_frame.grid(row=0)

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

        self.dismiss_button = Button(self.button_frame, text="Dismiss",
                                     command=partial(self.leave, parameter), bg='grey', fg='white',
                                     font='Arial 12 bold', relief=FLAT)
        self.dismiss_button.grid(row=0, column=0, padx=(0, 5), pady=10)

        self.form_quad = Button(self.button_frame, text="Set as Exemplar",
                                command=lambda: self.form_quad_eq(parameter), relief=FLAT,
                                bg='grey', fg='white', font="Arial 12 bold")
        self.form_quad.grid(row=0, column=1)
        if parameter.string_set.get() == "(x+#)(x+#)":
            self.form_quad.configure(state=DISABLED)

    def form_quad_eq(self, parameter):
        parameter.string_set.set("(x+#)(x+#)")
        self.form_quad.configure(state=DISABLED)

    def leave(self, parameter):
        self.newFrame.destroy()

        parameter.help_button.config(state=NORMAL)


root = Tk()
root.title("Rectangle Questions")
app = rectangle(root)
root.mainloop()


