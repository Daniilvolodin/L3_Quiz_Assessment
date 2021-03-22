from tkinter import *
import random


class Quadratics_Entry:
    def __init__(self):
        self.random_1, self.random_2 = random.randrange(1, 10), random.randint(1, 6)
        self.symbols = ["+", "-"]
        self.symbol_random_1, self.symbol_random_2 = random.choice(self.symbols), random.choice(self.symbols)

        self.remaining_symbol_1 = self.symbols.index(self.symbol_random_1)
        self.counter_1 = self.symbols[self.remaining_symbol_1 - 1]

        self.remaining_symbol_2 = self.symbols.index(self.symbol_random_2)
        self.counter_2 = self.symbols[self.remaining_symbol_2 - 1]

        self.x_coefficient_1 = ['', 2, 3]
        self.coefficient_random_1 = random.choice(self.x_coefficient_1)

        self.x_coefficient_2 = ['', 2, 3]
        self.coefficient_random_2 = random.choice(self.x_coefficient_2)


already_answered = []


class Algebra_Entry:

    def __init__(self, parameter):
        self.repeated = False
        self.option_value = IntVar()
        self.parameter = parameter
        self.get_quad_entry = Quadratics_Entry()
        self.question_randomise = []

        font = "Arial 16 bold"
        t = "{}x²{}{}x{}{}"
        ###########################################################################################################

        x_cof_1 = self.get_quad_entry.coefficient_random_1

        if x_cof_1 == '':
            x_cof_1 = 1

        x_cof_2 = self.get_quad_entry.coefficient_random_2

        if x_cof_2 == '':
            x_cof_2 = 1

        random_1 = self.get_quad_entry.random_1
        random_symbol_1 = self.get_quad_entry.symbol_random_1
        if random_symbol_1 == '-':
            random_1 = -random_1

        random_2 = self.get_quad_entry.random_2
        random_symbol_2 = self.get_quad_entry.symbol_random_2
        if random_symbol_2 == '-':
            random_2 = -random_2

        # Correct
        a_value = x_cof_1 * x_cof_2

        b_value = (x_cof_1 * random_2) + (x_cof_2 * random_1)

        if b_value < 0:
            random_symbol_1 = ''

        if b_value >= 0:
            random_symbol_1 = '+'

        c_value = random_1 * random_2
        if c_value < 0:
            random_symbol_2 = ''
        if c_value >= 0:
            random_symbol_2 = '+'

        # Incorrect 1
        inc_sym_b_1, inc_sym_c_1 = "", ""
        inc_a_value_1 = x_cof_1 * x_cof_2
        inc_b_value_1 = (x_cof_1 * random_2) - (x_cof_2 * random_1)
        inc_c_value_1 = (random_1 * random_2)
        if inc_b_value_1 >= 0:
            inc_sym_b_1 = "+"
        if inc_c_value_1 >= 0:
            inc_sym_c_1 = "+"
        self.incorrect_answer_1 = t.format(inc_a_value_1, inc_sym_b_1,
                                           inc_b_value_1, inc_sym_c_1,
                                           inc_c_value_1)
        self.question_randomise.append(self.incorrect_answer_1)
        # Incorrect 2
        inc_sym_b_2, inc_sym_c_2 = "", ""
        inc_a_value_2 = x_cof_1 * x_cof_2
        inc_b_value_2 = (x_cof_1 * random_2) + (x_cof_2 * random_1)
        inc_c_value_2 = random_1 + random_2
        if inc_b_value_2 >= 0:
            inc_sym_b_2 = "+"
        if inc_c_value_2 >= 0:
            inc_sym_c_2 = "+"
        self.incorrect_answer_2 = t.format(inc_a_value_2, inc_sym_b_2,
                                           inc_b_value_2, inc_sym_c_2,
                                           inc_c_value_2)
        self.question_randomise.append(self.incorrect_answer_2)
        # Incorrect 3
        inc_sym_b_3, inc_sym_c_3 = "", ""
        inc_a_value_3 = x_cof_1 * x_cof_2
        inc_b_value_3 = (x_cof_1 * random_2) - (x_cof_2 * random_1)
        inc_c_value_3 = -(random_1 * random_2)
        if inc_b_value_3 >= 0:
            inc_sym_b_3 = "+"
        if inc_c_value_3 >= 0:
            inc_sym_c_3 = "+"
        self.incorrect_answer_3 = t.format(inc_a_value_3, inc_sym_b_3,
                                           inc_b_value_3, inc_sym_c_3,
                                           inc_c_value_3)
        self.question_randomise.append(self.incorrect_answer_3)
        # Expand variables

        self.correct_answer_1 = t.format(a_value, random_symbol_1, b_value, random_symbol_2, c_value)
        self.question_randomise.append(self.correct_answer_1)
        random.shuffle(self.question_randomise)

        ###########################################################################################################

        self.start_frame = Frame()
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.main_frame = Frame(self.start_frame, pady=10, bg='black', padx=10)
        self.main_frame.grid(row=0)

        self.question_label = Label(self.main_frame, padx=10, pady=10,
                                    text="({}x{}{})({}x{}{})".format(self.get_quad_entry.coefficient_random_1,
                                                                     self.get_quad_entry.symbol_random_1,
                                                                     self.get_quad_entry.random_1,
                                                                     self.get_quad_entry.coefficient_random_2,
                                                                     self.get_quad_entry.symbol_random_2,
                                                                     self.get_quad_entry.random_2), font="Arial 32 bold"
                                    )
        self.question_label.grid(row=0)
        self.option_1 = Radiobutton(self.main_frame, text="{}".format(self.question_randomise[0]),
                                    value=1, variable=self.option_value, font=font,
                                    command=lambda: self.enable_submit()
                                    )
        self.option_1.grid(row=1, pady=3, sticky=NSEW)

        self.option_2 = Radiobutton(self.main_frame, text="{}".format(self.question_randomise[1]),
                                    value=2, variable=self.option_value, font=font,
                                    command=lambda: self.enable_submit()
                                    )
        self.option_2.grid(row=2, pady=3, sticky=NSEW)

        self.option_3 = Radiobutton(self.main_frame, text="{}".format(self.question_randomise[2]),
                                    value=3, variable=self.option_value, font=font,
                                    command=lambda: self.enable_submit()
                                    )
        self.option_3.grid(row=3, pady=3, sticky=NSEW)

        self.option_4 = Radiobutton(self.main_frame, text="{}".format(self.question_randomise[3]),
                                    value=4, variable=self.option_value, font=font,
                                    command=lambda: self.enable_submit()
                                    )
        self.option_4.grid(row=4, pady=3, sticky=NSEW)

        self.submit_button = Button(self.main_frame, text="Submit", command=lambda: self.check_answer(),
                                    state=DISABLED
                                    )
        self.submit_button.grid(row=5, pady=3, sticky=NSEW)
        self.question_randomise.sort()

        for x in range(len(already_answered)):
            if self.question_randomise in already_answered:
                self.repeated = True
        if self.repeated is True:
            self.start_frame.destroy()
            Algebra_Entry(self)
            already_answered.remove(self.question_randomise)

    def check_answer(self):
        var = self.option_value.get()
        if self.question_randomise[var - 1] == \
                self.question_randomise[self.question_randomise.index(self.correct_answer_1)]:
            print("Correct Answer")
        else:
            print("Incorrect Answer")

        self.start_frame.destroy()
        self.question_randomise.sort()

        already_answered.append(self.question_randomise)
        Algebra_Entry(self)

    def enable_submit(self):
        self.submit_button.configure(state=NORMAL)


root = Tk()
root.geometry("500x500")
root.title("Quadratics Practice")
app = Algebra_Entry(root)
root.mainloop()

