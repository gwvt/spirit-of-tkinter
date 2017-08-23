import tkinter as tk
from time import sleep
from threading import Thread

from settings import settings


class CrackleFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # set square side to 20 pixels
        self.square_side = 20

        self.canvas = self.make_canvas()
        self.canvas.grid(row=0, column=0)

        # draw square
        self.square = self.canvas.create_rectangle(
                    self.square_side, self.square_side,
                    self.square_side * 2, self.square_side * 2,
                    fill=settings.colors['Black'])

        # create button to start moving square
        self.start_button = self.make_start_button()
        self.start_button.grid(row=1, column=0)

    # run animation on separate thread
    def start_moving(self):
        self.crackling_thread = Thread(
            target=self.move_square)
        self.crackling_thread.start()

    # move square along x-axis or y-axis
    def move_square(self):
        for i in range(0, 7):
            sleep(.3)
            if i % 2 == 0:
                self.canvas.move(self.square, self.square_side, 0)
            else:
                self.canvas.move(self.square, 0, self.square_side)

    def make_start_button(self):
        start_button = tk.Button(
            self,
            text='Crackle',
            command=self.start_moving)
        settings.button_standard_config(start_button)

        return start_button

    def make_canvas(self):
        canvas_side = canvas_side = 16 * self.square_side
        canvas = tk.Canvas(self)
        canvas.configure(width=canvas_side,
                         height=canvas_side)
        return canvas
