import tkinter as tk

app = tk.Tk()


# define classes to create multiple frames and buttons
class ButtonFrame(tk.Frame):
    def __init__(self, parent):
        # create instance of tk.Frame as self
        super().__init__(parent)
        self.configure(bd=10, relief='raised')


class BlueButton(tk.Button):
    # create button instance with parent and text
    def __init__(self, parent, text):
        super().__init__(parent)

        # define plain function, not instance method, to pass to lambda
        def make_parent_blue():
            # get the widget's parent to configure
            parent = self.master
            parent.configure(bg='blue')

        # configure widget with options passed to __init__ function
        self.configure(text=text)

        # and common values for all instances
        self.configure(command=make_parent_blue, fg='red')


frame1 = ButtonFrame(app)
frame1.grid(row=0, column=0)

frame2 = ButtonFrame(app)
frame2.grid(row=0, column=1)

button1 = BlueButton(frame1, 'Make my parent blue')
button1.grid()

button2 = BlueButton(frame2, 'No, make my parent blue')
button2.grid()

app.mainloop()
