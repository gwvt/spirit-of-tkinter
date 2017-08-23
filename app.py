import tkinter as tk

app = tk.Tk()


def make_it_blue(widget):
    widget.configure(bg='blue')


frame = tk.Frame(app)

frame.configure(bd=10, relief='raised')
frame.grid()

button = tk.Button(
    frame, text='Sing it', command=lambda: make_it_blue(frame))
button.grid()

app.mainloop()
