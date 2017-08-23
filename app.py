import tkinter as tk

# create root window
app = tk.Tk()

# add button widget with text
# give it app as parent with first argument
# return widget from constructor
button = tk.Button(app, text='A Button')

# place button widget in the grid of its parent
button.grid()

# start main event loop
app.mainloop()
