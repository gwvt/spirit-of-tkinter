import tkinter as tk

app = tk.Tk()

# create canvas widget with dimensions
canvas = tk.Canvas(app, width=400, height=400)
canvas.grid()

# call methods on canvas widget to draw shape object
# pass coordinates x0, y0, x1, y1 of rectangle bounding the oval
# coordinates are from top left corner of canvas
# no parent because the method is not creating a new widget
circle = canvas.create_oval(50, 50, 350, 350)

# call itemconfigure method on canvas widget to configure the shape object
# passed as first argument
canvas.itemconfigure(
    circle,
    fill='yellow',
    outline='black'
)

app.mainloop()
