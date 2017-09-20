import tkinter as tk
from functools import partial


# define Settings class to be available across multiple classes/widgets
# define custom color palette
class Settings():
    def __init__(self):
        self.colors = {
            'Yellow': '#ffe132',
            'Red': '#ff1313',
            'Orange': '#ff9936',
            'Blue': '#14d0f0',
            'Green': '#11c300',
            'Grey': '#CCCCCC',
            'Black': '#000000',
            'White': '#FFFFFF'
        }


# use label frame as parent to canvas and frames for buttons
class ColorsFrame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # configure text and location for label
        self.configure(
            labelanchor='nw', text='Light show!')

        # create inner frame to control layout
        self.inner_frame = tk.Frame(self, padx=10, pady=10)
        self.inner_frame.grid()

        self.canvas_side = 375
        self.canvas_pad = self.canvas_side * .1

        # call method to make canvas
        # follow convention of naming custom methods with 'make_'
        # to avoid collisions with tkinter 'create_' methods
        self.canvas = self.make_canvas()
        self.canvas.grid(row=0, column=0)

        # call method to draw circle
        self.circle = self.make_circle('White')

        # call method to make button frames
        self.circle_button_frame = self.make_button_frame('Circle')
        self.circle_button_frame.grid(row=0, column=1)

        self.background_button_frame = self.make_button_frame('Background')
        self.background_button_frame.grid(row=1, column=0)

        # define plain functions to pass to make_button method
        def fill_background(color):
            self.canvas.configure(bg=settings.colors[color])

        def fill_circle(color):
            self.canvas.itemconfigure(
                self.circle,
                fill=settings.colors[color],
                outline=settings.colors[color])

        # iterate over colors to generate buttons
        # pass above functions to command option to
        # determine the target of the color change
        # place background buttons across columns,
        # circle buttons across rows
        for index, key in enumerate(settings.colors):
            self.make_button(
                self.background_button_frame,
                0,
                index,
                key,
                fill_background)
            self.make_button(
                self.circle_button_frame,
                index,
                0,
                key,
                fill_circle)

    def make_canvas(self):
        canvas = tk.Canvas(self.inner_frame)
        canvas.configure(
            width=self.canvas_side, height=self.canvas_side)
        canvas.configure(bg=settings.colors['White'])

        return canvas

    def make_circle(self, color):
        circle = self.canvas.create_oval(
            self.canvas_pad,
            self.canvas_pad,
            self.canvas_side - self.canvas_pad,
            self.canvas_side - self.canvas_pad)
        self.canvas.itemconfigure(
            circle,
            fill=settings.colors[color],
            outline=settings.colors[color])

        return circle

    def make_button_frame(self, label):
        button_frame = tk.LabelFrame(self.inner_frame)
        button_frame.configure(
            labelanchor='n', text=label, padx=5, pady=5)
        return button_frame

    # use radio buttons with background color but neither text nor indicator to
    # create a series of clickable colors
    def make_button(
            self, parent, row, column, color, command):
        button = tk.Radiobutton(
            parent, indicatoron=0, bd=0,
            # use [functools.]partial to create closure over each
            # iteration of the loop
            command=partial(command, color))
        button.configure(
                    # width in characters, height in text lines
                    width=5,
                    height=2,
                    bg=settings.colors[color])
        button.grid(
            row=row, column=column)


# instantiate settings object
settings = Settings()

app = tk.Tk()

# instantiate label frame with app as parent
app.colors_frame = ColorsFrame(app)
app.colors_frame.grid()

app.mainloop()
