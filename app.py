import tkinter as tk

from frames.colors import ColorsFrame
from frames.quit import QuitFrame
from frames.pictures import PicturesFrame
from frames.shapes import ShapesFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(padx=10, pady=10)

        self.shapes_frame = ShapesFrame(self)
        self.shapes_frame.grid(row=0, column=0, columnspan=2)

        self.colors_frame = ColorsFrame(self)
        self.colors_frame.grid(row=1, column=0)

        self.pictures_frame = PicturesFrame(self)
        self.pictures_frame.grid(row=1, column=1)

        self.quit_frame = QuitFrame(self)
        self.quit_frame.grid(row=2, column=0, columnspan=2)


app = App()
app.title('The Spirit of Tkinter')
app.mainloop()
