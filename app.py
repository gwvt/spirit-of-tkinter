import tkinter as tk

app = tk.Tk()


def print_it():
    print('And the men who hold high places must be the ones to start.')


# pass function object to button with command option
# call function by clicking on button
button = tk.Button(app, text='Sing it', command=print_it)

button.grid()

app.mainloop()
