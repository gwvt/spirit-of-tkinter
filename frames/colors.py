import tkinter as tk
from functools import partial

from settings import settings


class ColorsFrame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(
            labelanchor='nw', text='Light show!')

        self.inner_frame = tk.Frame(self, padx=10, pady=10)
        self.inner_frame.grid()

        self.canvas_side = 375
        self.canvas_pad = self.canvas_side * .1

        self.canvas = self.make_canvas()
        self.canvas.grid(row=0, column=0)

        self.circle = self.make_circle('White')

        self.circle_button_frame = self.make_button_frame('Circle')
        self.circle_button_frame.grid(row=0, column=1)

        self.background_button_frame = self.make_button_frame('Background')
        self.background_button_frame.grid(row=1, column=0)

        def fill_background(color):
            self.canvas.configure(bg=settings.colors[color])

        def fill_circle(color):
            self.canvas.itemconfigure(
                self.circle,
                fill=settings.colors[color],
                outline=settings.colors[color])

        for index, key in enumerate(settings.colors.keys()):
            self.make_button(
                self.background_button_frame,
                0,
                index,
                key,
                fill_background)
            self.make_button(
                self.circle_button_frame,
                index,
                0,
                key,
                fill_circle)

    def make_canvas(self):
        canvas = tk.Canvas(self.inner_frame)
        canvas.configure(
            width=self.canvas_side, height=self.canvas_side)
        canvas.configure(bg=settings.colors['White'])

        return canvas

    def make_circle(self, color):
        circle = self.canvas.create_oval(
            self.canvas_pad,
            self.canvas_pad,
            self.canvas_side - self.canvas_pad,
            self.canvas_side - self.canvas_pad)
        self.canvas.itemconfigure(
            circle,
            fill=settings.colors[color],
            outline=settings.colors[color])

        return circle

    def make_button_frame(self, label):
        button_frame = tk.LabelFrame(self.inner_frame)
        button_frame.configure(
            labelanchor='n', text=label, padx=5, pady=5)
        return button_frame

    def make_button(
            self, parent, row, column, color, command):
        button = tk.Radiobutton(
            parent, indicatoron=0, bd=0,
            command=partial(command, color))
        button.configure(
                    width=5,
                    height=2,
                    bg=settings.colors[color])
        button.grid(
            row=row, column=column)
