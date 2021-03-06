import tkinter as tk

from settings import settings


class ShapesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(padx=40)

        self.dimensions = self.set_dimensions(600, 200, 4, 100, 100)

        self.canvas = self.make_canvas()
        self.canvas.grid(row=0, column=0)

        self.shape_features = self.set_shape_features()
        self.current_shapes = []

        self.shape_number_menu = self.make_shape_number_menu()
        self.shape_number_menu.grid(row=0, column=1)

    def set_dimensions(
        self, canvas_width, canvas_height, shape_number,
            shape_width, shape_height):

        dimensions = {
            'canvas_width': canvas_width,
            'canvas_height': canvas_height,
            'shape_number': shape_number,
            'shape_width': shape_width,
            'shape_height': shape_height,
            'shape_padx': (
                ((canvas_width - (shape_number * shape_width)) / shape_number)
                * (shape_number / (shape_number + 1))),
            'shape_pady': (canvas_height - shape_height) / 2
        }

        return dimensions

    def make_canvas(self):
        canvas = tk.Canvas(self)
        canvas.configure(width=self.dimensions['canvas_width'],
                         height=self.dimensions['canvas_height'])

        return canvas

    def set_shape_features(self):
        features = {
            'shape': None,
            'fill': None,
            'outline': None,
            'coordinates_descriptor': None
        }
        return features

    def make_shape_number_menu(self):
        self.shape_number_var = tk.IntVar()

        shape_number_menu = tk.OptionMenu(
            self, self.shape_number_var, 2, 4, 8)
        self.shape_number_var.set(4)

        self.shape_number_var.trace(
            'w',
            lambda *args: self.change_shape_number(
                self.shape_number_var.get()))

        return shape_number_menu

    def change_shape_number(self, shape_number):
        if shape_number == 2 or shape_number == 4:
            shape_width = 100
            shape_height = 100
        elif shape_number == 8:
            shape_width = 50
            shape_height = 50

        self.dimensions = self.set_dimensions(
            self.dimensions['canvas_width'],
            self.dimensions['canvas_height'],
            shape_number,
            shape_width,
            shape_height)

        self.make_shapes(
            self.shape_features['shape'],
            self.shape_features['fill'],
            self.shape_features['outline'],
            self.shape_features['coordinates_descriptor'])

    def select_shape(self, event):
        if event.char == '1':
            self.make_shapes('oval', 'White', 'Black', 'outer_corners')
        elif event.char == '2':
            self.make_shapes('oval', 'White', 'Black', 'top_half')
        elif event.char == '3':
            self.make_shapes('oval', 'White', 'Black', 'bottom_half')
        elif event.char == '4':
            self.make_shapes('rectangle', 'White', 'Black', 'outer_corners')
        elif event.char == '5':
            self.make_shapes('rectangle', 'White', 'Black', 'top_half')
        elif event.char == '6':
            self.make_shapes('rectangle', 'White', 'Black', 'bottom_half')
        elif event.char == '7':
            self.make_shapes('polygon', 'White', 'Black', 'full_isosceles_up')
        elif event.char == '8':
            self.make_shapes(
                'polygon', 'White', 'Black', 'top_half_isosceles_up')
        elif event.char == '9':
            self.make_shapes(
                'polygon', 'White', 'Black', 'bottom_half_isosceles_down')
        elif event.char == '0':
            self.make_shapes(None, None, None, None)

    def get_coordinates(self, index, descriptor):
        if descriptor is None:
            return

        coordinates = {
            'outer_corners': {
                'x0': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) + (
                        self.dimensions['shape_padx']),
                'y0': self.dimensions['shape_pady'],
                'x1': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) + (
                    self.dimensions['shape_padx'] +
                    self.dimensions['shape_width']),
                'y1':
                    self.dimensions['shape_pady'] +
                    self.dimensions['shape_height']
            },
            'top_half': {
                'x0': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) +
                    self.dimensions['shape_padx'],
                'y0': self.dimensions['shape_pady'],
                'x1': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) + (
                    self.dimensions['shape_padx'] +
                    self.dimensions['shape_width']),
                'y1': self.dimensions['shape_pady'] +
                    self.dimensions['shape_height'] / 2
            },
            'bottom_half': {
                'x0': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) +
                    self.dimensions['shape_padx'],
                'y0': self.dimensions['shape_pady'] +
                    self.dimensions['shape_height'] / 2,
                'x1': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) +
                    self.dimensions['shape_padx'] +
                    self.dimensions['shape_width'],
                'y1': self.dimensions['shape_pady'] +
                    self.dimensions['shape_height']
            },
            'full_isosceles_up': {
                'x0': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) + (
                    self.dimensions['shape_width'] / 2) +
                    self.dimensions['shape_padx'],
                'y0': self.dimensions['shape_pady'],
                'x1': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) +
                    self.dimensions['shape_padx'],
                'y1': self.dimensions['shape_pady'] +
                    self.dimensions['shape_height'],
                'x2': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) + (
                    self.dimensions['shape_padx'] +
                    self.dimensions['shape_width']),
                'y2': self.dimensions['shape_pady'] +
                    self.dimensions['shape_height'],
            },
            'top_half_isosceles_up': {
                'x0': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) + (
                    self.dimensions['shape_width'] / 2) +
                    self.dimensions['shape_padx'],
                'y0': self.dimensions['shape_pady'],
                'x1': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) +
                    self.dimensions['shape_padx'],
                'y1': (self.dimensions['shape_pady'] +
                       self.dimensions['shape_height'] / 2),
                'x2': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) + (
                    self.dimensions['shape_padx'] +
                    self.dimensions['shape_width']),
                'y2': (self.dimensions['shape_pady'] +
                       self.dimensions['shape_height'] / 2),
            },
            'bottom_half_isosceles_down': {
                'x0': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) + (
                    self.dimensions['shape_width'] / 2) +
                    self.dimensions['shape_padx'],
                'y0': self.dimensions['shape_pady'] +
                    self.dimensions['shape_height'],
                'x1': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) +
                    self.dimensions['shape_padx'],
                'y1': (self.dimensions['shape_pady'] +
                       self.dimensions['shape_height'] / 2),
                'x2': index * (
                    self.dimensions['shape_width'] +
                    self.dimensions['shape_padx']) + (
                    self.dimensions['shape_padx'] +
                    self.dimensions['shape_width']),
                'y2': (self.dimensions['shape_pady'] +
                       self.dimensions['shape_height'] / 2),
            },
        }

        return coordinates[descriptor]

    def make_one_shape(self, shape, fill, outline, *args):
        name_create_function = 'create_{}'.format(shape)
        shape = getattr(self.canvas, name_create_function)(
            *args,
            fill=settings.colors[fill],
            outline=settings.colors[outline]
        )

        return shape

    def make_shapes(self, shape, fill, outline, coordinates_descriptor):
        for current_shape in self.current_shapes:
            self.canvas.delete(current_shape)

        self.shape_features['shape'] = shape
        self.shape_features['fill'] = fill
        self.shape_features['outline'] = outline
        self.shape_features['coordinates_descriptor'] = coordinates_descriptor

        self.current_shapes = []

        if shape is not None:
            for i in range(0, self.dimensions['shape_number']):
                self.current_shapes.append(
                    self.make_one_shape(
                        shape, fill, outline,
                        list(
                            self.get_coordinates(
                                i, coordinates_descriptor)
                            .values())))
