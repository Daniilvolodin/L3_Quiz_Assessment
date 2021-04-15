from tkinter import *
import re
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
        self.start_frame.place(relx=0.5, rely=0.5, relheight=1, relwidth=1, anchor=CENTER)

        self.quest_entry = Frame(self.start_frame)
        self.quest_entry.grid(row=0)

        self.simplified = Entry(self.quest_entry, justify=CENTER)
        self.simplified.grid(row=0)

        self.check_sub = Button(self.quest_entry, text="CHECK",
                                bg='grey', fg='white',
                                font="Arial 10 bold", command=lambda: self.check_regex())
        self.check_sub.grid(row=1, sticky=NSEW, pady=(4, 0))

    def check_regex(self):
        check_answer = re.search("[(]x[+\-][\d]{1,3}[)][(]x[+\-][\d]{1,3}[)]",
                                 self.simplified.get())
        if check_answer:
            print("OK")
        else:
            print("NOT OK")


if __name__ == "__main__":
    root = Tk()
    app = recQuest(root)
    root.title("Rectangle Questions")
    root.mainloop()


