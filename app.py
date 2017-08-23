import tkinter as tk

from frames.shapes import ShapesFrame
from frames.lyrics import LyricsFrame
from frames.colors import ColorsFrame
from frames.crackle import CrackleFrame
from frames.pictures import PicturesFrame
from frames.quit import QuitFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(padx=10, pady=10)

        self.shapes_frame = ShapesFrame(self)
        self.shapes_frame.grid(row=0, column=0)

        self.lyrics_frame = LyricsFrame(self)
        self.lyrics_frame.grid(row=0, column=1)

        self.colors_frame = ColorsFrame(self)
        self.colors_frame.grid(row=1, column=0, rowspan=2)

        # add crackle frame
        self.crackle_frame = CrackleFrame(self)
        self.crackle_frame.grid(row=1, column=1)

        self.pictures_frame = PicturesFrame(self)
        self.pictures_frame.grid(row=2, column=1)

        self.quit_frame = QuitFrame(self)
        self.quit_frame.grid(row=3, column=0, columnspan=2)

        self.bind_events()

    def bind_events(self):
        self.bind('<Key>', self.direct_key_events)

        self.lyrics_frame.search_box.bind(
            '<FocusIn>', self.lyrics_frame.search_box_focus_in)

        self.bind(
            '<Button-1>', self.lyrics_frame.search_box_focus_out)

        self.lyrics_frame.search_box.bind(
            '<Return>', self.lyrics_frame.search_lyrics)

    def direct_key_events(self, event):
        if self.focus_get() == self.lyrics_frame.search_box:
            if event.keysym == 'Tab':
                self.lyrics_frame.search_box_focus_out(event)
            return

        if event.keysym == 'Left':
            if self.lyrics_frame.line_index > 0:
                self.lyrics_frame.move_to_adjacent_line(-1)
        elif event.keysym == 'Right':
            if self.lyrics_frame.line_index < (
                    len(self.lyrics_frame.lyrics) - 1):
                self.lyrics_frame.move_to_adjacent_line(1)
        elif event.char.isdigit():
            self.shapes_frame.select_shape(event)


app = App()
app.title('The Spirit of Tkinter')
app.mainloop()
