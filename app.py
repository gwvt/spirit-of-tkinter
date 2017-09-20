import tkinter as tk

app = tk.Tk()


def print_it():
    print('The world is, the world is -- love and life are deep.')


# create a frame widget with app as parent
frame = tk.Frame(app)

# pass in options with configure method
# with borderwidth in pixels and relief style of raised
frame.configure(bd=10, relief='raised')
frame.grid()

# create button with frame as parent
button = tk.Button(
    frame, text='Sing it', command=print_it)
button.grid()

app.mainloop()
