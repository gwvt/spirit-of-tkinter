import tkinter as tk

# create root window
app = tk.Tk()

# add button widget with text
# return widget from constructor
button = tk.Button(app, text='A Button')

# place button widget in the grid of its parent, the root window
button.grid()

# start main event loop
app.mainloop()
