import ctypes
import random
from tkinter import *
from export_window import ResultsExportTxt


def list_clear(x, y, z):
    for list_1 in [x, y, z]:
        list_1.clear()


def check_operator(x):
    if x >= 0:
        return "+" + str(x)

    else:
        return str(x)


def remove_one(x):
    if x == 1:
        x = ''
        return x
    else:
        return x


# Adjusts screen to be 600 by 500
# and align it in the middle.
def set_size(x):
    # Grabs user screen aspects (resolution)
    height = int((ctypes.windll.user32.GetSystemMetrics(0) / 2) - 400)
    width = int(ctypes.windll.user32.GetSystemMetrics(1) / 2 - 350)
    x.state('normal')
    return x.geometry("800x700+{}+{}".format(height, width))


scale = 1
font_scale = 1

transparent = '#787878'

label_config = {
    'bg': '#787878',
    'font': 'helvetica 25 bold',
    'fg': 'white'

}

label_config_2 = {
    'bg': '#787878',
    'font': 'helvetica 13 bold',
    'fg': 'white'

}

button_config = {
    'bg': 'white',
    'fg': 'black',
    'relief': 'flat',
    'font': ('helvetica', 12 * scale, 'bold'),
    'activebackground': 'black',
    'activeforeground': 'white'
}

settings_label = {'bg': transparent,
                  'fg': 'white',
                  'font': 'Helvetica 25 underline'}

timer_buttons = {
    'font': 'Helvetica 10',
    'relief': 'flat'
}

two_point_q_label = {
    'bg': transparent,
    'fg': 'white'
}

entry_two_point_q = {
    'font': 'Helvetica 12',
    'justify': 'center'
}

q3_text = {
    'font': 'Helvetica 12 bold',
    'bg': transparent,
    'fg': 'white'

}

q3_entry = {
    'font': 'Helvetica 12',
    'justify': 'center',
    'relief': 'flat',
    'highlightthickness': 1,
    'highlightbackground': 'black',
    'highlightcolor': '#cccccc'

}

q3_button = {
    'relief': 'flat',
    'font': 'helvetica 12 bold'
}

back_button = {
    'text': 'Back',
    'bg': 'white',
    'fg': 'black',
    'relief': 'flat',
    'font': ('helvetica', 12 * scale, 'bold'),
    'activebackground': 'black',
    'activeforeground': 'white'

}

set_2_red = {
    'highlightbackground': 'red',
    'highlightcolor': 'red'
}

set_2_norm = {
    'highlightbackground': 'black',
    'highlightcolor': '#cccccc'
}

warning_labels = {
    'font': 'helvetica 13 bold',
    'fg': '#f78981',
    'text': '',
    'bg': transparent
}

next_button_design = {
    'relief': 'flat',
    'font': 'helvetica 10 bold'
}

timer_design = {
    'font': 'helvetica 16 underline',
    'fg': 'white',
    'bg': transparent

}

radio_button_design = {
    'font': 'helvetica 18 bold',
    'bg': 'white',
    'activebackground': 'black',
    'activeforeground': 'white',
    'fg': 'black',

}

results_config = {
    'font': 'Arial 10 bold',
    'bg': 'white'
}
questions_remaining = 10

correct = []

incorrect = []

user_answers = []

randomized_question_gen = []

seconds_left = 0

minutes_left = 0

time = [minutes_left, seconds_left]

already_answered = []


class RandomizeAll:
    def __init__(self):
        self.acceptable = [random.randrange(-9, -1), random.randrange(1, 9)]


class ResultsExport:
    def __init__(self, parameter):

        self.parameter = parameter

        self.start_frame = Frame(bg='black', padx=3, pady=3)
        self.start_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.content_frame = Frame(self.start_frame, bg='white')
        self.content_frame.grid(row=0)

        self.results_label = Label(self.content_frame, text='Results', font='helvetica 18 underline',
                                   justify=CENTER, bg='white')
        self.results_label.grid(row=0, sticky=NSEW, pady=(0, 30))

        self.incorrect_score = Label(self.content_frame, text='Incorrect: %d' % len(incorrect),
                                     **results_config)
        self.incorrect_score.grid(row=1, sticky=NSEW)

        self.correct_score = Label(self.content_frame, text='Correct: %d' % len(correct),
                                   **results_config)
        self.correct_score.grid(row=2, sticky=NSEW)

        self.frame = Frame(self.content_frame, bg='white')
        self.frame.grid(row=3)

        for x in range(len(user_answers)):
            question = 'Question {}: {}' .format((x+1), user_answers[x])

            self.label = Label(self.frame, text=question, **results_config)
            self.label.grid(row=x)

        self.export_button = Button(self.content_frame, text='Export Results', font='Helvetica 13 bold',
                                    bg='grey', command=lambda: self.to_export(), fg='white')
        self.export_button.grid(row=4, pady=10)

    def to_export(self):
        self.start_frame.destroy()
        ResultsExportTxt()


class timerCount:
    def __init__(self, parameter):
        self.parameter = parameter
        self.frame = Frame(bg=transparent)
        self.frame.place(relx=0.5, rely=0.95, anchor=CENTER)

        self.timer = Label(self.frame, text='Time remaining: %d:%d' % (time[0], time[1]), **timer_design)
        self.timer.grid(row=0)

        self.timer.after(1000, lambda: self.update_time())

    def update_time(self):
        if time[0] >= 0:
            time[1] -= 1
            if time[1] < 0:
                time[0] -= 1
                time[1] = 59

            self.timer.configure(text='Time remaining: %d:%d' % (time[0], time[1]), **timer_design)

            self.timer.after(1000, lambda: self.update_time())
        if time[0] < 0:

            for x in range(10 - len(user_answers)):
                incorrect.append('Incorrect')
                user_answers.append('Your Answer Was: blank')
            self.stop()

        if questions_remaining <= 0:
            self.frame.destroy()

    def stop(self):
        self.timer.destroy()
        ResultsExport(self)
