from question1_options import *
from question3_two_points import *
from tkinter import ttk


questions = [TwoPointQ, OptionPick]


class StartContent:
    def __init__(self, parameter):
        self.menu_frame = Frame()
        self.parameter = parameter
        self.menu_frame.place(relx=0.025, rely=0.025)
        self.menu_button = Button(self.menu_frame, **button_config,
                                  text='Menu Button', command=lambda: self.to_menu_screen(self.parameter))
        self.menu_button.grid(row=0, ipady=10 * scale, ipadx=10 * scale)

        self.alg_quiz_frame = Frame(bg=transparent)
        self.alg_quiz_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.alg_quiz_label = Label(self.alg_quiz_frame, text='Algebra Quiz', **label_config)
        self.alg_quiz_label.grid(row=0, pady=(0, 15 * scale))

        self.alg_quiz_button = Button(self.alg_quiz_frame, text='Start Quiz', **button_config,
                                      command=lambda: self.start_quiz(), state=DISABLED)
        self.alg_quiz_button.grid(row=1, ipadx=20 * scale, ipady=5 * scale)
        if time[0] >= 1:
            self.enable_quiz()

    def enable_button(self):
        self.alg_quiz_button.configure(state=NORMAL)

    def to_menu_screen(self, parameter):
        self.menu_frame.destroy()
        self.alg_quiz_frame.destroy()
        MenuScreen(parameter)

    def start_quiz(self):
        self.menu_frame.destroy()
        self.alg_quiz_frame.destroy()
        timerCount(self)
        questions[0](self)

    def enable_quiz(self):
        self.alg_quiz_button.configure(state=NORMAL)


class MenuScreen:
    def __init__(self, parameter):
        self.full_screen = IntVar()
        self.menu_s_frame = Frame(bg=transparent)
        self.parameter = parameter
        self.menu_s_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.menu_content_frame = Frame(self.menu_s_frame, bg=transparent)
        self.menu_content_frame.grid(row=0)

        self.value_windowed = IntVar()

        self.menu_label = Label(self.menu_content_frame, text='Menu', **settings_label)
        self.menu_label.grid(row=0, sticky=NSEW)

        self.style = ttk.Style()
        self.change_res_slide = ttk.Checkbutton(self.menu_content_frame, text='Full Screen', offvalue=0,
                                                onvalue=1, variable=self.full_screen)
        self.style.configure('TCheckbutton', background=transparent, foreground='white',
                             font='helvetica 12 bold')
        self.change_res_slide.grid(row=1, sticky=NSEW)
        self.with_title_bar = ttk.Radiobutton(self.menu_content_frame, text='With Title Bar',
                                              value=0, variable=self.value_windowed)

        self.with_title_bar.grid(row=2, sticky=NSEW)

        self.without_title_bar = ttk.Radiobutton(self.menu_content_frame, text='Without Title Bar',
                                                 value=1, variable=self.value_windowed)
        self.style.configure('TRadiobutton', background=transparent, foreground='white',
                             font='helvetica 12 bold')
        self.without_title_bar.grid(row=3, sticky=NSEW)

        self.set_timer_btn = Button(self.menu_content_frame, text='Set Timer',
                                    **timer_buttons, command=lambda: self.to_timer(self.parameter))

        self.set_timer_btn.grid(row=4, sticky=NSEW, pady=10)

        self.apply_settings = Button(self.menu_content_frame, text='Apply Settings',
                                     **timer_buttons, command=lambda: self.adjust())
        self.apply_settings.grid(row=5, sticky=NSEW)

        self.back_btn = Button(**back_button,
                               command=lambda: self.back_menu(self.parameter))
        self.back_btn.place(relx=0.025, rely=0.025)

    def adjust(self):
        if self.full_screen.get() == 1:
            self.parameter.state('zoomed')
        if self.full_screen.get() == 0:
            set_size(x=self.parameter)
        if self.value_windowed.get() == 1:
            self.parameter.overrideredirect(1)
        if self.value_windowed.get() == 0:
            self.parameter.overrideredirect(0)

    def back_menu(self, parameter):
        self.menu_s_frame.destroy()
        self.back_btn.destroy()
        self.menu_content_frame.destroy()
        StartContent(parameter)

    def to_timer(self, parameter):
        self.menu_s_frame.destroy()
        self.menu_content_frame.destroy()
        self.back_btn.destroy()
        setTimer(parameter)


class setTimer:
    def __init__(self, parameter):
        self.parameter = parameter
        self.minute_var = IntVar()
        self.second_var = IntVar()

        self.starter_frame = Frame(bg=transparent)
        self.starter_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.timer_label = Label(self.starter_frame, text='Set Time', **settings_label)
        self.timer_label.grid(row=0)

        self.time_display = Label(self.starter_frame, text='%d:%d' % (time[0], time[1]),
                                  bg=transparent,
                                  fg='white', font='Helvetica 20')
        self.time_display.grid(row=1, pady=20)

        self.button_frame = Frame(self.starter_frame, bg=transparent)
        self.button_frame.grid(row=2, pady=3)

        self.minute_button = Button(self.button_frame, text='Add minute', **timer_buttons,
                                    command=lambda: self.min_configure())
        self.minute_button.grid(row=0, column=0, padx=(0, 3))

        self.second_button = Button(self.button_frame, text='Add 10 seconds', **timer_buttons,
                                    command=lambda: self.sec_configure())
        self.second_button.grid(row=0, column=1)

        self.set_default = Button(self.starter_frame, text='Set to default', **timer_buttons,
                                  command=lambda: self.default_set())
        self.set_default.grid(row=3, sticky=NSEW, pady=(0, 3))

        self.back_button = Button(**back_button, command=lambda: self.back_to_menu())
        self.back_button.place(relx=0.025, rely=0.025)

        self.reset = Button(self.starter_frame, text='Reset Time', **timer_buttons,
                            command=lambda: self.reset_time(), state=DISABLED)
        self.reset.grid(row=5, sticky=NSEW)

    def back_to_menu(self):
        self.starter_frame.destroy()
        self.button_frame.destroy()
        self.back_button.destroy()
        MenuScreen(self.parameter)

    def reset_time(self):
        for x in range(len(time)):
            time[x] = 0
        self.time_display.configure(text='%d:%d' % (time[0], time[1]))
        self.reset.configure(state=DISABLED)
        self.minute_button.configure(state=NORMAL)
        self.second_button.configure(state=NORMAL)

    def min_configure(self):
        # time[0] = min
        # time [1] = sec
        self.reset.configure(state=NORMAL)
        time[0] += 1
        self.time_display.configure(text='%d:%d' % (time[0], time[1]))

        if time[0] == 60:
            time[1] = 0
            for button in [self.minute_button, self.second_button]:
                button.configure(state=DISABLED)
            self.time_display.configure(text='%d:%d' % (time[0], time[1]))

    def sec_configure(self):
        time[1] += 10
        self.reset.configure(state=NORMAL)
        if time[1] >= 60:
            time[1] = 0
            time[0] += 1
        if time[0] >= 60:
            for button in [self.minute_button, self.second_button]:
                button.configure(state=DISABLED)
            time[1] = 0
            time[0] = 60

        self.time_display.configure(text='%d:%d' % (time[0], time[1]))

    def default_set(self):
        time[0] = 15
        time[1] = 30
        self.reset.configure(state=NORMAL)
        for button in [self.minute_button, self.second_button]:
            button.configure(state=NORMAL)
        self.time_display.configure(text='%d:%d' % (time[0], time[1]))
