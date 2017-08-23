import tkinter as tk

app = tk.Tk()

# create canvas with dimensions
canvas = tk.Canvas(app, width=400, height=400)
canvas.grid()

# call methods on canvas object to draw shape
# pass coordinates x0, y0, x1, y1 of rectangle bounding the oval
# no parent because the method is not creating a new widget
circle = canvas.create_oval(50, 50, 350, 350)

# call itemconfigure method on canvas object to configure the shape
canvas.itemconfigure(
    circle,
    fill='yellow',
    outline='black'
)

app.mainloop()
