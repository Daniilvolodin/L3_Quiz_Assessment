from lists_and_dictionaries import *
import lists_and_dictionaries


# GUI window has an entry and a button
# checks if entry input matches regular expressions
# If valid, the program will close and create a filename
# with user input.
# Otherwise it will continue on asking for an input.
class ResultsExportTxt:
    def __init__(self):
        self.new_frame = Frame(bg=lists_and_dictionaries.transparent)
        self.new_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.both = Frame(self.new_frame, bg=lists_and_dictionaries.transparent)
        self.both.grid(row=0)
        self.entry = Entry(self.both, font='helvetica 12 italic',
                           justify=CENTER)
        self.entry.grid(row=0)
        # submits user input and checks whether it's valid or not
        self.button = Button(self.both, text='SUBMIT', **lists_and_dictionaries.button_config,
                             command=lambda: self.check_regex())
        self.button.grid(row=1, sticky=NSEW, pady=(10, 0))
        self.warning_label = Label(self.new_frame, font='Arial 16 italic', fg='#f78981',
                                   bg=lists_and_dictionaries.transparent)
        self.warning_label.grid(row=1)

    def check_regex(self):
        check = self.entry.get()

        problem = ''
        for v in check:
            # if input is valid, the program continues
            if re.match(r'[A-Za-z1-90]', v):
                continue
            # if input is empty, the message will
            # be set to warn user that it cannot contain
            # blank spaces

            if v == ' ':
                problem = 'No blank spaces'
            # Cannot contain symbols
            else:
                problem = 'No Symbols Such As ' + str(v)
            break
        # File name cannot be left blank
        if check == '':
            problem = 'File name cannot be left empty'
        # show warning message if there is a problem
        if problem != '':
            self.warning_label.configure(text=problem)
            return
        # otherwise, the program creates a text file
        # with user results
        else:
            self.warning_label.configure(text='Clear', fg='green')
            filename = str(self.entry.get())+'.txt'
            f = open(filename, 'w+')
            for x in range(len(lists_and_dictionaries.user_answers)):
                f.write('Question %d:' % (x+1) + lists_and_dictionaries.user_answers[x] + '  ' + '\n\n')

            f.read()
            f.close()
            quit()
