import tkinter as tk

app = tk.Tk()

canvas = tk.Canvas(app, width=400, height=400)
canvas.grid()

circle = canvas.create_oval(50, 50, 350, 350)

canvas.itemconfigure(
    circle,
    fill='yellow',
    outline='black'
)

app.mainloop()
