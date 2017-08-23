import tkinter as tk


class LyricsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(padx=20, bd=5, relief='raised')

        # load lyrics lines text into list
        self.lyrics = self.load_lyrics()

        # add inner frame and text entry box
        self.search_box_frame = tk.Frame(self, width=150, height=50)
        self.search_box_frame.grid_propagate(False)
        self.search_box_frame.grid(row=0, column=0)

        self.search_box = self.make_search_box()
        self.search_box.grid()

        # add inner frame and message widget to display text
        self.line_message_frame = tk.Frame(self, width=250, height=50)
        self.line_message_frame.grid_propagate(False)
        self.line_message_frame.grid(row=0, column=1)

        self.line_message = self.make_line_message()
        self.line_message.grid()

        # initialize index of lyrics list and display line
        self.line_index = 0
        self.display_line()

    def load_lyrics(self):
        self.lyrics_file = open('files/lyrics.txt', 'r')
        lyrics_list = []
        for line in self.lyrics_file:
            stripped_line = line.rstrip()
            lyrics_list.append(stripped_line)
        lyrics_list.insert(0, '')

        return lyrics_list

    def make_search_box(self):
        # create special Tkinter StringVar variable and associate with
        # user input in Entry widget
        self.search_string_var = tk.StringVar(value='search lyrics')

        search_box = tk.Entry(
            self.search_box_frame, width=12, fg='Grey',
            textvariable=self.search_string_var)
        return search_box

    def make_line_message(self):
        line_message = tk.Message(self.line_message_frame, width=250, text='')
        return line_message

    def display_line(self):
        self.line_message.configure(text=self.lyrics[self.line_index])

    # move back or forward one line with key event left or right arrow
    def move_to_adjacent_line(self, plus_minus_one):
        self.line_index += plus_minus_one
        self.display_line()

    # change value and font color of entry box based on focus in or out
    def search_box_focus_in(self, event):
        self.search_string_var.set('')
        self.search_box.configure(fg='Black')

    def search_box_focus_out(self, event):
        if hasattr(event, 'keysym') and event.keysym == 'Tab' or (
                hasattr(event, 'widget') and (
                    event.widget is not self.search_box)):
            self.clear_search_box()

    # clear search box -- called when exiting focus or
    # executing search function
    def clear_search_box(self):
        self.search_string_var.set('search lyrics')
        self.search_box.configure(fg='Grey')
        self.focus_set()

    def search_lyrics(self, event):
        self.search_result(self.search_string_var)
        self.search_box_focus_out(None)

    # display line of lyrics
    def search_result(self, search_string_var):
        search_string = search_string_var.get()
        for index, line in enumerate(self.lyrics):
            if search_string.lower() in line.lower():
                self.line_index = index
                self.display_line()
                break
            self.clear_search_box()
