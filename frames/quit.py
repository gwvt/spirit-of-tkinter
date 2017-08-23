import tkinter as tk

from settings import settings


class QuitFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(padx=10, pady=10)

        self.inner_frame = tk.Frame(self)
        self.inner_frame.configure(
            bd=4, relief='ridge', padx=10, pady=10, bg='Grey')

        self.inner_frame.grid()

        self.quit_button = tk.Button(self.inner_frame, text='Turn it off',
                                     command=self.quit)
        settings.button_standard_config(self.quit_button)
        self.quit_button.grid()
