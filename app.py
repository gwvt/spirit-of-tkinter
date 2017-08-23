import tkinter as tk

app = tk.Tk()


def print_it():
    print('And the men who hold high places must be the ones to start.')


# pass function to button with command option
button = tk.Button(app, text='Sing it', command=print_it)

button.grid()

app.mainloop()
