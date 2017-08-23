import tkinter as tk

# import from settings module
from settings import settings


class QuitFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(padx=10, pady=10)

        # create inner_frame for styling and padding
        self.inner_frame = tk.Frame(self)
        self.inner_frame.configure(
            bd=4, relief='ridge', padx=10, pady=10, bg='Grey')

        self.inner_frame.grid()

        self.quit_button = tk.Button(self.inner_frame, text='Turn it off',
                                     command=self.quit)
        # set standard configuration for button
        settings.button_standard_config(self.quit_button)
        self.quit_button.grid()
