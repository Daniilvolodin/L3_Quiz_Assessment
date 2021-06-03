from lists_and_dictionaries import *
import menu_btn_contents
import lists_and_dictionaries


def exit_quiz():
    quit()


class OptionPick:
    def __init__(self, parameter):
        self.parameter = parameter
        self.minutes = minutes_left
        self.seconds = seconds_left

        self.coefficient_pick = [1, 2, 3]

        self.x1 = random.choice(self.coefficient_pick)
        self.x2 = random.choice(self.coefficient_pick)

        self.ran1 = check_operator(x=random.choice(RandomizeAll().acceptable))
        self.ran2 = check_operator(x=random.choice(RandomizeAll().acceptable))

        self.question = "({}x{})({}x{})".format(remove_one(x=self.x1), self.ran1, remove_one(x=self.x2),
                                                self.ran2)
        already_answered.append(self.question)
        self.ran1 = int(self.ran1)
        self.ran2 = int(self.ran2)

        self.operators = ['+', '-']

        self.a_op = remove_one(x=self.x1 * self.x2)
        self.b_op = check_operator(x=(self.x1 * self.ran2) + (self.x2 * self.ran1))
        self.c_op = check_operator(x=(self.ran1 * self.ran2))

        self.alt_b_value = check_operator(x=int(self.b_op) - (2 * (self.x2 * self.ran2)))

        self.correct = "%sx²%sx%s" % (self.a_op, self.b_op, self.c_op)

        self.incorrect_1 = "{}x²{}x{}".format(self.a_op, str(self.b_op).replace(str(self.b_op)[0],
                                              self.operators[self.operators.index(str(self.b_op)[0]) - 1]),
                                              check_operator(x=-(self.ran1 * self.ran2)))
        self.incorrect_2 = "{}x²{}x{}".format(self.a_op, self.b_op, check_operator(x=self.ran1 + self.ran2))
        self.incorrect_3 = "{}x²{}x{}".format(self.a_op, self.alt_b_value, self.c_op)

        self.shuffle_questions = [self.correct, self.incorrect_1, self.incorrect_2, self.incorrect_3]
        random.shuffle(self.shuffle_questions)

        self.user_pick = IntVar()

        self.border_start = Frame(padx=3, pady=3, bg='black')
        self.border_start.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.start_frame = Frame(self.border_start, bg='white', pady=10, padx=10)
        self.start_frame.grid(row=0)

        self.question_label = Label(self.start_frame, bg='white', font='helvetica 25 bold', text=self.question)
        self.question_label.grid(row=0)

        self.option_frame = Frame(self.start_frame, bg='white')
        self.option_frame.grid(row=1, pady=(20, 0))

        self.f1 = Frame(self.option_frame, bg='black', bd=2)
        self.f1.grid(row=0, pady=5)
        self.f2 = Frame(self.option_frame, bg='black', bd=2)
        self.f2.grid(row=1, pady=5)
        self.f3 = Frame(self.option_frame, bg='black', bd=2)
        self.f3.grid(row=2, pady=5)
        self.f4 = Frame(self.option_frame, bg='black', bd=2)
        self.f4.grid(row=3, pady=5)
        self.option_1 = Radiobutton(self.f1, variable=self.user_pick, value=1,
                                    text=self.shuffle_questions[0], command=lambda: self.activate_next(),
                                    **radio_button_design)
        self.option_2 = Radiobutton(self.f2, variable=self.user_pick, value=2,
                                    text=self.shuffle_questions[1], command=lambda: self.activate_next(),
                                    **radio_button_design)
        self.option_3 = Radiobutton(self.f3, variable=self.user_pick, value=3,
                                    text=self.shuffle_questions[2], command=lambda: self.activate_next(),
                                    **radio_button_design)
        self.option_4 = Radiobutton(self.f4, variable=self.user_pick, value=4,
                                    text=self.shuffle_questions[3], command=lambda: self.activate_next(),
                                    **radio_button_design)

        self.option_1.grid(row=0)
        self.option_2.grid(row=1)
        self.option_3.grid(row=2)
        self.option_4.grid(row=3)

        self.next_button = Button(text="Next", command=lambda: self.check_answer(), state=DISABLED,
                                  **next_button_design)
        self.next_button.place(relx=0.95, rely=0.95, anchor=CENTER)

        self.quit_button = Button(text='Quit Program', command=lambda: exit_quiz(),
                                  **next_button_design)
        self.quit_button.place(relx=0.1, rely=0.95, anchor=CENTER)

        self.border_start.after((time[0] * 1000 * 60) + time[1] * 1000, lambda: self.remove_all())

        while len(set(already_answered)) != len(already_answered):
            print("Dupe")
            already_answered.remove(already_answered[-1])
            self.border_start.destroy()
            OptionPick(self)

    def remove_all(self):
        self.border_start.destroy()
        self.next_button.destroy()

    def activate_next(self):
        self.next_button.configure(state=NORMAL)

    def check_answer(self):

        if self.user_pick.get() - 1 == self.shuffle_questions.index(self.correct):
            correct.append("Correct")
            user_answers.append("Correct")

        else:
            incorrect.append("Incorrect")
            user_answers.append("Your Answer Was: %s\n"
                                "Correct Answer: %s" % (self.shuffle_questions[self.user_pick.get()-1], self.correct))

        lists_and_dictionaries.questions_remaining -= 1

        if lists_and_dictionaries.questions_remaining <= 0:
            self.remove_all()
            ResultsExport(self)
        else:
            menu_btn_contents.questions[0](self)
            self.next_button.destroy()
            self.border_start.destroy()
            self.quit_button.destroy()
