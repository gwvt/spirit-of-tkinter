import tkinter as tk
from functools import partial

from settings import settings


class PicturesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(width=300, height=350)

        self.names = ['Geddy', 'Alex', 'Neil', 'Rush', 'Clear']

        # iterate over list of names to generate text for button
        # and path to image file
        for i in range(0, len(self.names)):
            self.make_button(i, self.names[i])

        self.select_image('Clear')

    # pass select_image function to partial with closure over path to
    # each image file
    def select_image(self, text):
        if hasattr(self, 'image_label'):
            self.image_label.destroy()

        image_path = 'images/{}.gif'.format(text.lower())
        image = tk.PhotoImage(file=image_path)

        self.image_label = tk.Label(self, image=image)
        # re-assign image to image_label
        # see http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        self.image_label.image = image
        self.image_label.grid(row=0, column=0, columnspan=len(self.names))

    def make_button(self, column, text):
        button = tk.Button(
            self, text=text,
            command=partial(self.select_image, text))
        settings.button_standard_config(button)
        button.grid(row=1, column=column, sticky=tk.N+tk.S+tk.E+tk.W)
