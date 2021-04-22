from tkinter import *
import re

# No symbols
# No blank spaces
# No spaces

data = []


class export:
    def __init__(self, parameter):
        self.parameter = parameter

        self.mainFrame = Frame()
        self.mainFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.button_frame = Frame(self.mainFrame)
        self.button_frame.grid(row=0)

        self.button_incorrect = Button(self.button_frame, text='Incorrect', font='Arial 16 bold',
                                       command=lambda: data.append('Incorrect'))
        self.button_incorrect.grid(row=0, column=0)

        self.button_correct = Button(self.button_frame, text='Correct', font='Arial 16 bold',
                                     command=lambda: data.append('Correct'))
        self.button_correct.grid(row=0, column=1)

        self.export_button = Button(self.mainFrame, text='Export', font='Arial 16 italic',
                                    command=lambda: self.to_stat())
        self.export_button.grid(row=1, sticky=NSEW)

    def to_stat(self):
        self.mainFrame.destroy()
        export_stat()


class export_stat:
    def __init__(self):
        self.new_frame = Frame()
        self.valid_char = r'[A-Za-z1-9]'

        self.new_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.both = Frame(self.new_frame)
        self.both.grid(row=0)
        self.entry = Entry(self.both, font='helvetica 12 italic',
                           justify=CENTER)
        self.entry.grid(row=0)

        self.button = Button(self.both, text='SUBMIT', font='Arial 13 bold',
                             bg='grey', fg='white', command=lambda: self.check_regex())
        self.button.grid(row=1, sticky=NSEW, pady=(10, 0))

        self.warning_label = Label(self.new_frame, font='Arial 16 italic', fg='red')
        self.warning_label.grid(row=1)

    def check_regex(self):
        check = self.entry.get()
        problem = ''
        for v in check:
            if re.match(r'[A-Za-z1-9]', v):
                continue
            if v == '':
                problem = 'No blank spaces'
            else:
                problem = 'No Symbols Such As ' + str(v)
            break

        if check == '':
            problem = 'Cannot be blank'

        if problem != '':
            self.warning_label.configure(text=problem)
            return

        else:
            self.warning_label.configure(text='Clear', fg='green')
            filename = str(self.entry.get())+'.txt'
            f = open(filename, 'w+')
            for x in data:
                f.write(str(x) + '\n')
            f.read()
            f.close()
            self.new_frame.destroy()
            export(self)


root = Tk()
root.geometry("360x380")
app = export(root)
root.mainloop()
