import tkinter as tk
from time import sleep
from threading import Thread

from settings import settings


class CrackleFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pattern_side = 8
        self.square_side = 20

        self.canvas = self.make_canvas()
        self.canvas.grid(row=0, column=0)

        self.start_button = self.make_start_button()
        self.start_button.grid(row=1, column=0)

        self.crackling = False

    def make_canvas(self):
        canvas_side = canvas_side = (self.pattern_side + 2) * self.square_side
        canvas = tk.Canvas(self)
        canvas.configure(width=canvas_side,
                         height=canvas_side)
        return canvas

    def make_start_button(self):
        start_button = tk.Button(
            self,
            text='Crackle',
            command=self.toggle_crackling)
        settings.button_standard_config(start_button)

        return start_button

    def toggle_crackling(self):
        if self.crackling is False:
            self.crackling = True
            self.start_button.configure(
                highlightbackground=settings.colors['Black'],
                fg=settings.colors['White'])
            square = self.canvas.create_rectangle(
                self.square_side, self.square_side,
                self.square_side * 2, self.square_side * 2,
                fill=settings.colors['Black'])
            self.crackling_thread = Thread(
                target=self.make_crackle, args=(square, 0, 8, True, True))
            self.crackling_thread.start()
        else:
            self.start_button.configure(
                highlightbackground=settings.colors['White'],
                fg=settings.colors['Black'])
            self.crackling = False

    def make_crackle(
            self, square, position, side_length, x_axis_changing, ascending):
        if self.crackling is False:
            self.canvas.delete(square)
            return
        sleep(.0587)
        if x_axis_changing is True and ascending is True:
            if position == side_length - 1:
                self.canvas.move(square, 0, self.square_side)
                return self.make_crackle(square, 1, side_length, False, True)
            else:
                self.canvas.move(square, self.square_side, 0)
                return self.make_crackle(
                    square, position + 1, side_length, True, True)
        elif x_axis_changing is False and ascending is True:
            if position == side_length - 1:
                self.canvas.move(square, -self.square_side, 0)
                return self.make_crackle(square, 1, side_length, True, False)
            else:
                self.canvas.move(square, 0, self.square_side)
                return self.make_crackle(
                    square, position + 1, side_length, False, True)
        elif x_axis_changing is True and ascending is False:
            if position == side_length - 1:
                self.canvas.move(square, 0, -self.square_side)
                return self.make_crackle(square, 1, side_length, False, False)
            else:
                self.canvas.move(square, -self.square_side, 0)
                return self.make_crackle(
                    square, position + 1, side_length, True, False)
        elif x_axis_changing is False and ascending is False:
            if position == side_length - 1:
                self.canvas.move(square, self.square_side, 0)
                return self.make_crackle(square, 1, side_length, True, True)
            else:
                self.canvas.move(square, 0, -self.square_side)
                return self.make_crackle(
                    square, position + 1, side_length, False, False)
