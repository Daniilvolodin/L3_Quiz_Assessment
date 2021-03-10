from tkinter import *
from functools import partial


class mainGUI:
    def __init__(self, partner):

        font = "Arial 16 bold"

        self.value = IntVar()
        self.partner = partner

        # Radio Buttons (Quiz Options)
        self.opt_rad_1 = Radiobutton(padx=10, pady=10,
                                     value=1, variable=self.value, bg="black",
                                     text='Quiz Option 1', fg="green",
                                     font=font)
        self.opt_rad_1.pack(side=TOP, pady=10)

        self.opt_rad_2 = Radiobutton(padx=10, pady=10,
                                     value=2, variable=self.value, bg="black",
                                     text='Quiz Option 2', fg="green", font=font)
        self.opt_rad_2.pack(side=TOP, pady=10)

        self.opt_rad_3 = Radiobutton(padx=10, pady=10,
                                     value=3, variable=self.value, bg="black",
                                     text='Quiz Option 3', fg="green", font=font)
        self.opt_rad_3.pack(side=TOP, pady=10)


if "__main__" == __name__:
    root = Tk()
    root.resizable(True, True)
    app = mainGUI(root)
    root.title("New")
    root.state("zoomed")
    root.mainloop()
