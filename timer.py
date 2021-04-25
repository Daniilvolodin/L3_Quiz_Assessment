from tkinter import *


class time_GUI:
    def __init__(self, parameter):
        self.parameter = parameter

        # Starting amount of seconds and minutes
        self.minutes = 0
        self.seconds = 0
        # Starting frame / holds the contents
        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.time_frame = Frame(self.start_frame)
        self.time_frame.grid(row=0)

        # Time label / shows minutes and seconds
        self.time_label = Label(self.time_frame, text="{}:{}".format(self.minutes, self.seconds),
                                font='Arial 30 italic')
        self.time_label.grid(row=0)

        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=1)

        # Button adds a minute to a timer
        self.set_minutes = Button(self.button_frame, text='ADD MINUTE',
                                  command=lambda: self.add_minutes())
        self.set_minutes.grid(row=0, column=0)
        # Button adds ten seconds to a timer
        self.set_seconds = Button(self.button_frame, text='ADD 10 SECONDS',
                                  command=lambda: self.add_seconds())
        self.set_seconds.grid(row=0, column=1)
        # Starts the countdown timer / disabled at the start
        self.start_button = Button(self.start_frame, text='START', command=lambda: self.update(),
                                   state=DISABLED)
        self.start_button.grid(row=2, sticky=NSEW)

    # Function adds ten seconds and updates label display
    def add_seconds(self):
        self.seconds += 10
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
        self.time_label.configure(text="{}:{}".format(self.minutes, self.seconds))
        # Enables start button
        self.start_button.configure(state=NORMAL)

    # Function adds a minute and refreshes label display
    def add_minutes(self):
        self.minutes += 1
        self.time_label.configure(text="{}:{}".format(self.minutes, self.seconds))
        self.start_button.configure(state=NORMAL)

    # Function starts the timer
    def update(self):
        set_b = [self.set_seconds, self.set_minutes]
        self.start_button.configure(state=DISABLED)
        # Disables all the buttons
        for button in set_b:
            button.configure(state=DISABLED)
        # Refreshes time label
        self.time_label.configure(text="{}:{}".format(self.minutes, self.seconds))
        # when second amount is 0, program
        # deducts a minute and sets seconds to 60
        if self.seconds == 0:
            self.minutes -= 1
            self.seconds = 60
        self.seconds -= 1
        # When minute and second count is 0, the timer stops
        if self.seconds == 0 and self.minutes == 0:
            self.time_label.configure(text="{}:{}".format(self.minutes, self.seconds))
            # Enables second and minute buttons
            for button in set_b:
                button.configure(state=NORMAL)

        else:
            # Countdown timer uses .after()
            # that has two parameters, one of them
            # is defines the time to invoke something
            # in second parameter by using milliseconds
            self.time_label.after(1000, lambda: self.update())


if __name__ == "__main__":
    root = Tk()
    # Set new icon
    photo = PhotoImage(file='iconchip.png')
    root.iconphoto(False, photo)
    gui = time_GUI(root)
    root.geometry("300x300")
    root.title('Hello')
    root.mainloop()

