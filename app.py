import tkinter as tk

app = tk.Tk()


def print_it():
    print('The world is, the world is -- love and life are deep.')


frame = tk.Frame(app)


frame.configure(bd=10, relief='raised')
frame.grid()


button = tk.Button(
    frame, text='Sing it', command=print_it)
button.grid()

app.mainloop()
