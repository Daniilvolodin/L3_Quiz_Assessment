from tkinter import *
from tkinter import ttk
import ctypes


# Adjusts screen to be 600 by 500
# and align it in the middle.
def set_size():
    # Grabs user screen aspects (resolution)
    height = int((ctypes.windll.user32.GetSystemMetrics(0) / 2) - 300)
    width = int(ctypes.windll.user32.GetSystemMetrics(1) / 2 - 250)
    root.state('normal')

    return root.geometry("600x500+{}+{}".format(height, width))


# main window where user can change
# his screen settings
class change_res:
    def __init__(self, parameter):
        self.parameter = parameter

        self.entry_font = {'font': ('helvetica', 11)}

        # Variable stores user choice for whether
        # he wants his screen to be windowed or not
        self.int_var = IntVar()

        # Variable stores user choice
        # for whether he wants to have a full screen or not
        self.num_var = IntVar()

        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.opt_frame = Frame(self.start_frame)
        self.opt_frame.grid(row=0)

        self.label_resolution = ttk.Label(self.opt_frame, text="Resolution", **self.entry_font)
        self.label_resolution.grid(row=0, column=0)

        # Checkbutton should be 'checked' for the window
        # to be in full screen
        self.resolution_menu = ttk.Checkbutton(self.opt_frame, text="Full screen",
                                               variable=self.num_var, onvalue=1,
                                               offvalue=0)
        self.resolution_menu.grid(row=0, column=1, sticky=NSEW)

        self.radio_frame = Frame(self.start_frame)
        self.radio_frame.grid(row=1)

        self.windowed = ttk.Label(self.radio_frame, text='Windowed')
        self.windowed.grid(row=0, column=0)
        # choose yes for the window to have a title bar
        self.yes_button = ttk.Radiobutton(self.radio_frame, text='Yes', value=0,
                                          variable=self.int_var)
        self.yes_button.grid(row=0, column=1)
        # choose no for the window to have no title bar
        self.no_button = ttk.Radiobutton(self.radio_frame, text='No', value=1,
                                         variable=self.int_var)
        self.no_button.grid(row=0, column=2)
        # Press Submit to set the window options
        self.submit_res = ttk.Button(self.start_frame, text='SUBMIT',
                                     command=lambda: self.on_submit())
        self.submit_res.grid(row=2, sticky=NSEW)

    def on_submit(self):
        # If user have checked checkbutton,
        # the window will cover the screen
        if self.num_var.get() == 1:
            root.state('zoomed')
        # If checkbutton is left unchecked, the
        # window will return to its original size
        if self.num_var.get() == 0:
            set_size()
        if self.int_var.get() == 1:
            root.overrideredirect(1)
        if self.int_var.get() == 0:
            root.overrideredirect(0)


if __name__ == "__main__":
    root = Tk()
    root.title("Resolution")
    set_size()
    app = change_res(root)
    root.mainloop()
# root.attributes("-full screen", True)
# root.state("zoomed")
# root.overrideredirect(1)
