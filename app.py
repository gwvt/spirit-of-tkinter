import tkinter as tk

# import frame classes from frames package
from frames import ColorsFrame, QuitFrame


# define class for main app
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(padx=10, pady=10)

        self.colors_frame = ColorsFrame(self)
        self.colors_frame.grid(row=0, column=0)

        self.quit_frame = QuitFrame(self)
        self.quit_frame.grid(row=1, column=0)


# instantiate main app
app = App()

# add title to window
app.title('The Spirit of Tkinter')

app.mainloop()
