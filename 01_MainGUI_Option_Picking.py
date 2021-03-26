from tkinter import *


# Object that creates a window
class template:

    # Initialises widgets within a window
    def __init__(self, parameter):
        self.parameter = parameter
        # Set up a variable
        self.get_value = IntVar()

        # 'gather' frame aligns all contents inside it
        # in the middle of the window
        self.gather = Frame()
        self.gather.place(relx=0.5, anchor=CENTER, rely=0.5)

        # Frame that holds title and buttons
        self.initial_frame = Frame(self.gather)
        self.initial_frame.grid()

        # Displays Quiz title
        self.quiz_name_label = Label(self.initial_frame, text="Quiz Testing",
                                     font="Arial 24 bold")
        self.quiz_name_label.grid(row=0, sticky=N)

        # Displays 3 options in a form of 'Radio' buttons
        self.radio_button_1 = Radiobutton(self.initial_frame, text="Option 1",
                                          value=1, variable=self.get_value,
                                          bg='grey', fg='blue', command=lambda: self.enable_submit())
        self.radio_button_1.grid(row=1, pady=(4, 0), padx=10)

        self.radio_button_2 = Radiobutton(self.initial_frame, text="Option 2",
                                          value=2, variable=self.get_value,
                                          bg='grey', fg='blue', command=lambda: self.enable_submit())
        self.radio_button_2.grid(row=2, pady=(4, 0), padx=10)

        self.radio_button_3 = Radiobutton(self.initial_frame, text="Option 3",
                                          value=3, variable=self.get_value,
                                          bg='grey', fg='blue', command=lambda: self.enable_submit())
        self.radio_button_3.grid(row=3, pady=(4, 0), padx=10)

        # Submit button that submits user option
        self.submit_button = Button(self.initial_frame, text="Submit", bg='#1b5b7a',
                                    fg='white', padx=13, command=lambda: self.direct_option(),
                                    state=DISABLED)
        self.submit_button.grid(row=4, pady=4)

        # Creates a warning label widget
        self.warning_label = Label(self.initial_frame)
        self.warning_label.grid(row=5, sticky=N)

        # Is a help button
        self.help_button = Button(self.initial_frame, text="Help?",
                                  font="Arial 12 bold", command=lambda: self.direct_help())
        self.help_button.grid(row=6, sticky=N)

    def enable_submit(self):
        self.submit_button.configure(state=NORMAL)

    # Directs user to a help window
    def direct_help(self):
        self.gather.destroy()
        toHelp()

    # Function responsible for directing user to the option screen
    # if user didn't pick any of the options, the program displays a warning
    def direct_option(self):
        variables = self.get_value.get()

        # If user picked one of the options, the program continues
        if variables > 0:
            self.gather.destroy()
            option_direct(self, variables)
        # If user didn't pick anything, the program displays a warning
        else:
            self.warning_label.configure(text="Pick One Of The Options Above", fg='red')


# Alternative version of a window that display user
# option of choice
class option_direct:

    # Initialises variables within a function
    def __init__(self, parameter, variable):
        self.parameter = parameter
        self.variable = variable

        # Aligns a frame and all the widgets within a frame
        # in the center of a window
        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Displays user picked option
        self.option_label = Label(self.start_frame, padx=10, pady=4, text="You Chose "
                                                                          "Option {}".format(variable))
        self.option_label.grid(row=0)

        self.return_button = Button(self.start_frame, padx=10, pady=4, text='Return',
                                    command=lambda: self.return_template())
        self.return_button.grid(row=1)

        # Is an exit button
        self.exit_button = Button(self.start_frame, padx=10, pady=4, text='Exit',
                                  command=lambda: quit())
        self.exit_button.grid(row=2, pady=(2, 0))

    # Function responsible for directing user to
    # the main screen
    def return_template(self):
        self.start_frame.destroy()
        template(self)


# Sets up a help window
class toHelp:
    def __init__(self):
        # Sets up a frame in the centre
        self.help_frame = Frame()
        self.help_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Help text
        self.help_label = Label(self.help_frame, text="Help text goes here",
                                font="Arial 16 italic")
        self.help_label.grid(row=0)

        # Return button
        self.return_help_button = Button(self.help_frame, text='Return to main screen',
                                         padx=3, pady=2, font='Arial 10 bold',
                                         bg='grey', command=lambda: self.to_main_screen())
        self.return_help_button.grid(row=1)

    # Function returns user to main Gui window
    def to_main_screen(self):
        self.help_frame.destroy()
        template(self)

# If the name of the file is the same as the
# main file
if __name__ == "__main__":
    root = Tk()
    root.title("Layout")
    root.geometry("300x300")
    app = template(root)
    root.mainloop()


