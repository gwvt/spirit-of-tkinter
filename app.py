import tkinter as tk

from frames.colors import ColorsFrame
from frames.quit import QuitFrame
# import pictures frame
from frames.pictures import PicturesFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(padx=10, pady=10)

        self.colors_frame = ColorsFrame(self)
        self.colors_frame.grid(row=0, column=0)

        # add pictures frame
        self.pictures_frame = PicturesFrame(self)
        self.pictures_frame.grid(row=0, column=1)

        # use columnspan option to center button
        self.quit_frame = QuitFrame(self)
        self.quit_frame.grid(row=1, column=0, columnspan=2)


app = App()
app.title('The Spirit of Tkinter')
app.mainloop()
