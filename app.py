import tkinter as tk
from functools import partial

app = tk.Tk()


def make_it_blue(widget):
    widget.configure(bg='blue')


frame = tk.Frame(app)

frame.configure(bd=10, relief='raised')
frame.grid()

# pass lambda to command option with frame as argument
button = tk.Button(
    frame, text='Make me blue', command=partial(make_it_blue, frame))
button.grid()

app.mainloop()
