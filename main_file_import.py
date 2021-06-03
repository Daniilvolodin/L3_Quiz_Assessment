from menu_btn_contents import *
from tkinter import *


# Main Class - Executes all the contents held in one
# library
class CompileProgram:

    def __init__(self, parameter):
        self.parameter = parameter

        # Directs program to the start GUI
        StartContent(self.parameter)


# Initiates tkinter library
# Changes default tkinter icon to an icon of
# personal preference.
if __name__ == "__main__":
    root = Tk()
    app = CompileProgram(root)
    root.title('Algebra Quiz')
    set_size(x=root)
    root.configure(bg='#787878')
    photo = PhotoImage(file='iconchip.png')
    root.iconphoto(False, photo)
    root.mainloop()
