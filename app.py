import tkinter as tk

# create root window
app = tk.Tk()

# add button widget with text
button = tk.Button(app, text='A Button')

# place button in the grid of its parent, the root window
button.grid()

app.mainloop()
