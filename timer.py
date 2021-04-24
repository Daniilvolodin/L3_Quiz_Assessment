from tkinter import *


class time_GUI:
    def __init__(self, parameter):
        self.parameter = parameter

        self.minutes = 0
        self.seconds = 0
        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.time_frame = Frame(self.start_frame)
        self.time_frame.grid(row=0)

        self.time_label = Label(self.time_frame, text="{}:{}".format(self.minutes, self.seconds),
                                font='Arial 30 italic')
        self.time_label.grid(row=0)

        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=1)

        self.set_minutes = Button(self.button_frame, text='ADD MINUTE',
                                  command=lambda: self.add_minutes())
        self.set_minutes.grid(row=0, column=0)

        self.set_seconds = Button(self.button_frame, text='ADD 30 SECONDS',
                                  command=lambda: self.add_seconds())
        self.set_seconds.grid(row=0, column=1)
        self.start_button = Button(self.start_frame, text='START', command=lambda: self.update())
        self.start_button.grid(row=2, sticky=NSEW)

    def add_seconds(self):
        self.seconds += 10
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
        self.time_label.configure(text="{}:{}".format(self.minutes, self.seconds))

    def add_minutes(self):
        self.minutes += 1
        self.time_label.configure(text="{}:{}".format(self.minutes, self.seconds))

    def update(self):
        set_b = [self.start_button, self.set_seconds,
                 self.set_minutes]
        for button in set_b:
            button.configure(state=DISABLED)

        self.time_label.configure(text="{}:{}".format(self.minutes, self.seconds))

        if self.seconds == 0:
            self.minutes -= 1
            self.seconds = 60
        self.seconds -= 1

        if self.seconds == 0 and self.minutes == 0:
            self.time_label.configure(text="{}:{}".format(self.minutes, self.seconds))
            for button in set_b:
                button.configure(state=NORMAL)

        else:
            self.time_label.after(1000, lambda: self.update())


if __name__ == "__main__":
    root = Tk()
    gui = time_GUI(root)
    root.geometry("300x300")
    root.title('Hello')
    root.mainloop()
