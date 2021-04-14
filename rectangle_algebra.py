from tkinter import *

# The area of a rectangle can be represented by
# e.g.3x²−4x−32
# exempli gratia
# Make user simplify quadratic
# Make user figure the sides of a rectangle
# Both questions asked must be in entry form


class recQuest:
    def __init__(self, parameter):

        self.parameter = parameter

        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.simplify_1 = Entry(self.start_frame)
        self.simplify_1.grid(row=0, column=1, sticky=NSEW)

if __name__ == "__main__":
    root = Tk()
    app = recQuest(root)
    root.title("Rectangle Questions")
    root.mainloop()

