import game
from tkinter import *


class Gui:
    def __init__(self, window):
        self.window = window

        # Radio buttons
        self.frame_levels = Frame(self.window)
        self.label_operation = Label(self.frame_levels, text='Pick A Difficulty')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_easy = Radiobutton(self.frame_levels, text='Easy', variable=self.radio_1, value=1,
                                      command=self.guesser)
        self.radio_normal = Radiobutton(self.frame_levels, text='Normal', variable=self.radio_1, value=2,
                                        command=self.guesser)
        self.radio_hard = Radiobutton(self.frame_levels, text='Hard', variable=self.radio_1, value=3,
                                      command=self.guesser)
        self.radio_impossible = Radiobutton(self.frame_levels, text='Impossible', variable=self.radio_1, value=4,
                                            command=self.guesser)
        self.label_operation.pack(side='left', padx=5)
        self.radio_easy.pack(side='left')
        self.radio_normal.pack(side='left')
        self.radio_hard.pack(side='left')
        self.radio_impossible.pack(side='left')
        self.frame_levels.pack(anchor='w', pady=10)

        # Guessed number
        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first)
        self.entry_guess = Entry(self.frame_first, width=40)
        self.label_first.pack(padx=20, side='left')
        self.entry_guess.pack(padx=20, side='left')
        self.frame_first.pack(anchor='w', pady=10)
        self.entry_guess.pack_forget()

        # Results label
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        # Compute button
        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='Guess', command=self.compute)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()

    def guesser(self):
        """
        Obtains your difficulty

        """
        self.entry_guess.delete(0, END)
        self.label_result.config(text='')
        self.entry_guess.pack()
        difficulty = self.radio_1.get()

        if difficulty == 1:
            self.label_first.config(text='Pick a number from 1 to 10')
        elif difficulty == 2:
            self.label_first.config(text='Pick a number from 1 to 100')
        elif difficulty == 3:
            self.label_first.config(text='Pick a number from 1 to 1000')
        elif difficulty == 4:
            self.label_first.config(text='Pick a number from 1 to 100000000000000000000')

    def compute(self):
        """
        Obtains the guessed number and your difficulty.
        Then, it checks if the guess is lower or higher than the correct number.
        If it is correct, then you win.
        The values must be numbers and positive.
        Otherwise, it raises errors.
        """
        try:
            guess = self.entry_guess.get()
            difficulty = self.radio_1.get()

            if difficulty == 1:
                if game.easy(guess) == 'lower' or game.easy(guess) == 'higher':
                    self.label_result.config(text=f'The answer is {game.easy(guess)} than {guess}')
                elif game.easy(guess):
                    self.label_result.config(text=f'{guess} is the answer. You win! Continue to normal mode.')

            elif difficulty == 2:
                if game.normal(guess) == 'lower' or game.normal(guess) == 'higher':
                    self.label_result.config(text=f'The answer is {game.normal(guess)} than {guess}')
                elif game.normal(guess):
                    self.label_result.config(text=f'{guess} is the answer. You win! Continue to hard mode.')

            elif difficulty == 3:
                if game.hard(guess) == 'lower' or game.hard(guess) == 'higher':
                    self.label_result.config(text=f'The answer is {game.hard(guess)} than {guess}')
                elif game.hard(guess):
                    self.label_result.config(text=f'{guess} is the answer. You win! Continue to impossible mode.')

            elif difficulty == 4:
                if game.impossible(guess) == 'lower' or game.impossible(guess) == 'higher':
                    self.label_result.config(text=f'The answer is {game.impossible(guess)} than {guess}')
                elif game.impossible(guess):
                    self.label_result.config(text=f'{guess} is the answer. You win! Thank you for playing.')

            else:
                self.label_result.config(text='No operation selected')

        except ValueError:
            self.label_result.config(text='Enter numeric values')

        except TypeError:
            self.label_result.config(text='Values must be positive')
