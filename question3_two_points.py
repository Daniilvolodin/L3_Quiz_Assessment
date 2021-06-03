# Icon source: https://www.cleanpng.com/png-question-mark-png-41220/
from lists_and_dictionaries import *
from functools import partial
import menu_btn_contents
import lists_and_dictionaries


# function generates warning messages that are
# appropriate to the given user input
# checks if user input is blank or contains
# forbidden characters
def check_root_error(value, message, num1, red):
    str(message)

    try:
        float(value.replace(' ', ''))

    except ValueError:

        if value.replace(' ', '') == '':
            message = 'Root %d entry cannot be blank' % num1
            red.configure(**set_2_red)
        else:
            message = 'Root %d entry cannot contain characters' % num1
            red.configure(**set_2_red)
        return message
    else:
        message = ''
        red.configure(**set_2_norm)
        return message
        pass


# Regular expression function that compares
# ordinary quadratic expression to user input
# if it doesn't match, the program will display warning message
def sim_ex(x, v):
    if not re.match(r'^\(x[+\-]\d*\)\(x[+\-]\d*\)$', v.get()):
        v.configure(**set_2_red)
        x.configure(text='Invalid Expression')
    else:
        v.configure(**set_2_norm)
        x.configure(text='')


# Two point question involves asking user for
# a simplified quadratic expression from a regular quadratic and
# its two roots.
class TwoPointQ:
    def __init__(self, parameter):

        self.parameter = parameter

        self.exemplar_variable = StringVar()

        self.random_num_1 = random.choice(RandomizeAll().acceptable)
        self.random_num_2 = random.choice(RandomizeAll().acceptable)

        # Contains a list of possible correct answers.
        self.correct_answers = ['(x{})(x{})'.format(check_operator(x=self.random_num_1),
                                                    check_operator(x=self.random_num_2)),
                                '(x{})(x{})'.format(check_operator(x=self.random_num_2),
                                                    check_operator(x=self.random_num_1)),
                                ]
        self.b_value = check_operator(x=(self.random_num_1 + self.random_num_2))
        self.c_value = check_operator(x=(self.random_num_1 * self.random_num_2))
        self.question_gen = "x²%sx%s" % (self.b_value, self.c_value)

        # Question generator variable
        self.question_prob = 'The quadratic expression\n' \
                             'is represented by: %s=0.\n ' \
                             'Find simplified quadratic form\n and define its roots' % self.question_gen
        already_answered.append(self.question_gen)

        self.start_frame = Frame(bg=transparent)
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.question_label = Label(self.start_frame, text=self.question_prob, **two_point_q_label,
                                    font='Helvetica 12 bold', wrap=240)
        self.question_label.grid(row=0)

        self.contents_frame = Frame(self.start_frame, bg=transparent)
        self.contents_frame.grid(row=1, sticky=NSEW, pady=(20, 0))

        self.simplified_ex_label = Label(self.contents_frame, text='Simplified expression:',
                                         **q3_text)
        self.simplified_ex_label.grid(row=0, column=0)

        self.simplified_ex_entry = Entry(self.contents_frame, **q3_entry, textvariable=self.exemplar_variable)
        self.simplified_ex_entry.grid(row=0, column=1, ipady=3)

        self.root_1_label = Label(self.contents_frame, text='Root 1:',
                                  **q3_text)
        self.root_1_label.grid(row=1, column=0, pady=10)

        self.root_1_entry = Entry(self.contents_frame, **q3_entry)
        self.root_1_entry.grid(row=1, column=1, ipady=3)

        self.root_2_label = Label(self.contents_frame, text='Root 2:', **q3_text)
        self.root_2_label.grid(row=2, column=0)

        self.root_2_entry = Entry(self.contents_frame, **q3_entry)
        self.root_2_entry.grid(row=2, column=1, ipady=3)

        self.buttons_frame = Frame(self.start_frame, bg=transparent)
        self.buttons_frame.grid(row=2, pady=(10, 0))

        self.check = Button(self.buttons_frame, text='Check', **q3_button,
                            command=lambda: self.check_input())
        self.check.grid(row=0, column=0, ipadx=70, ipady=3)

        self.question = Button(self.buttons_frame, text='?', **q3_button,
                               command=lambda: self.open_help(self))
        self.question.grid(row=0, column=1, ipadx=10, ipady=3, padx=(10, 0))

        self.warning_label = Label(self.start_frame, **warning_labels)
        self.warning_label.grid(row=3, pady=(10, 0))

        self.warning_label2 = Label(self.start_frame, **warning_labels)
        self.warning_label2.grid(row=4, pady=(3, 0))

        self.warning_label3 = Label(self.start_frame, **warning_labels)
        self.warning_label3.grid(row=5, pady=(3, 0))

        self.next_button = Button(text="Next", state=DISABLED, **next_button_design, padx=3,
                                  command=lambda: self.check_answer())
        self.next_button.place(relx=0.95, rely=0.95, anchor=CENTER)

        self.quit_button = Button(text='Quit Program', command=lambda: self.exit_quiz(),
                                  **next_button_design)
        self.quit_button.place(relx=0.1, rely=0.95, anchor=CENTER)

        # after specific amount of time, the question gui will get destroyed
        # and displayed user results despite him not finishing the quiz.
        self.start_frame.after((time[0] * 1000 * 60) + time[1] * 1000, lambda: self.remove_all())
        self.correct_comp = [-float(self.random_num_1), -float(self.random_num_2)]
        self.correct_comp.sort()

        # if there is a duplicate in a list of already answered questions
        # the program will update itself until it generates a question
        # that hasn't been answered
        while len(set(already_answered)) != len(already_answered):
            print("Dupe")
            already_answered.remove(already_answered[-1])
            self.start_frame.destroy()
            TwoPointQ(self)

    # Removes all the question contents including its
    # graphical interface
    def remove_all(self):
        self.start_frame.destroy()
        self.next_button.destroy()

    # Checking if user answer is right or wrong
    def check_answer(self):

        self.attempted = [float(self.root_1_entry.get()), float(self.root_2_entry.get())]
        self.attempted.sort()

        # if user answer is correct, the program will add it to particular lists
        # that will later display that data in results interface
        if self.simplified_ex_entry.get() in self.correct_answers and self.correct_comp == self.attempted:
            correct.append('Correct')
            user_answers.append("Correct")
            print('Correct comp:', self.correct_comp)
            print('Attempted:', self.attempted)
        # same function as above but correct is substituted with incorrect
        else:

            incorrect.append('Incorrect')
            user_answers.append("Your Answer Was: %s\n"
                                "Correct Answer: %s" % (self.simplified_ex_entry.get(), self.correct_answers[0]))
            print('Incorrect')
            print('Correct comp:', self.correct_comp)
            print('Attempted:', self.attempted)

        self.start_frame.destroy()
        self.next_button.destroy()
        self.quit_button.destroy()

        lists_and_dictionaries.questions_remaining -= 1

        print(lists_and_dictionaries.questions_remaining)
        print(self.correct_answers)

        # If there are no more questions left to answer, the program
        # will direct user to results interface.
        if lists_and_dictionaries.questions_remaining <= 0:
            self.remove_all()
            ResultsExport(self)
        # otherwise it will move user to multi-choice questions
        else:
            menu_btn_contents.questions[1](self)

    # compares user answer whether it's valid or not.
    def check_input(self):

        self.warning_label2.configure(text=check_root_error(value=self.root_1_entry.get(), message='', num1=1,
                                                            red=self.root_1_entry))
        self.warning_label3.configure(text=check_root_error(value=self.root_2_entry.get(), message='', num1=2,
                                                            red=self.root_2_entry))

        # Display warning message if user expression is wrong
        if not re.match(r'^\(x[+\-]\d*\)\(x[+\-]\d*\)$', self.simplified_ex_entry.get()):
            self.simplified_ex_entry.configure(**set_2_red)
            self.warning_label.configure(text='Invalid Expression')

        else:
            self.simplified_ex_entry.configure(**set_2_norm)
            self.warning_label.configure(fg=transparent)

            try:
                self.attempted = [float(self.root_1_entry.get()), float(self.root_1_entry.get())]
                self.attempted.sort()
            except ValueError:
                self.next_button.configure(state=DISABLED)
            else:
                self.next_button.configure(state=NORMAL)

    # Directs user to a help window
    def open_help(self, parameter):
        HelpWindow(parameter)
        self.question.configure(state=DISABLED)

    # Exits the quiz
    def exit_quiz(self):
        quit()
        self.parameter = partial


# Help window - Holds information about how to approach
# A two point question.
class HelpWindow:
    def __init__(self, parameter):
        self.parameter = parameter

        self.new_window = Toplevel(bg=transparent)
        photo2 = PhotoImage(file='question_symbol.png')
        self.new_window.iconphoto(False, photo2)
        self.new_window.title('Help')
        self.new_window.geometry('340x390')

        # Uses partial library so it can do both function simultaneously
        self.new_window.protocol("WM_DELETE_WINDOW", partial(self.leave, parameter))

        self.new_frame = Frame(self.new_window, bg=transparent)
        self.new_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.help_title = Label(self.new_frame, text='Help Index', bg=transparent,
                                font='Helvetica 20 bold', fg='white')
        self.help_title.grid(row=0)

        self.help_desc = Label(self.new_frame, text="Enter your answer in a form of "
                                                    "simplified quadratic equation\n\n"
                                                    "When using exemplars, change "
                                                    "hash tags to a number for "
                                                    "program to validate your input.", bg=transparent,
                               wrap=260, fg='white', font='helvetica 13 italic')
        self.help_desc.grid(row=1)

        self.button_frame = Frame(self.new_frame, bg=transparent)
        self.button_frame.grid(row=2, pady=(20, 0))

        self.set_exemplar = Button(self.button_frame, text='Set Exemplar', relief=FLAT,
                                   command=lambda: self.form_sim_eq(parameter))
        self.set_exemplar.grid(row=0, column=0, padx=(0, 10), ipady=3, ipadx=15)

        self.dismiss = Button(self.button_frame, text='Dismiss', relief=FLAT,
                              command=partial(self.leave, parameter)
                              )
        self.dismiss.grid(row=0, column=1, ipady=3, ipadx=15)

        if parameter.exemplar_variable.get() == '(x+#)(x+#)':
            self.set_exemplar.configure(state=DISABLED)

    # Adds a simplified quad. exemplar to user entry
    def form_sim_eq(self, parameter):
        parameter.exemplar_variable.set('(x+#)(x+#)')
        self.set_exemplar.configure(state=DISABLED)

    # Closes help window.
    def leave(self, parameter):
        self.new_window.destroy()
        parameter.question.config(state=NORMAL)
