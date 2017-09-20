import tkinter as tk

app = tk.Tk()


# define class to create multiple frames
class ButtonFrame(tk.Frame):
    def __init__(self, parent):
        # create instance of tk.Frame as self
        super().__init__(parent)
        self.configure(bd=10, relief='raised')


# define class to create multiple buttons
class BlueButton(tk.Button):
    # create button instance with parent and text
    def __init__(self, parent, text):
        super().__init__(parent)

        # define plain function, not instance method, to pass to command option
        def make_parent_blue():
            # get the widget's parent to call its configure method
            parent = self.master
            parent.configure(bg='blue')

        # configure created button widget with options passed
        # to __init__ function
        self.configure(text=text)
        # and with static values for all instances
        self.configure(command=make_parent_blue, fg='red')


# now use our custom classes instead of the native tkinter classes
# for creating frames and buttons
frame1 = ButtonFrame(app)
# place widget at specific location in grid
frame1.grid(row=0, column=0)

frame2 = ButtonFrame(app)
frame2.grid(row=0, column=1)

# create buttons with display text
button1 = BlueButton(frame1, 'Make my parent blue')
button1.grid()

button2 = BlueButton(frame2, 'No, make my parent blue')
button2.grid()

app.mainloop()
