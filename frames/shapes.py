import tkinter as tk

from settings import settings


class ShapesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(padx=40)

        self.dimensions = self.set_dimensions(600, 200, 4, 100, 100)

        self.canvas = self.make_canvas()
        self.canvas.grid()

        self.shape_features = self.set_shape_features()
        self.current_shapes = []

        self.make_shapes('polygon', 'White', 'Black', 'full_isosceles_up')

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

    def get_coordinates(self, index, descriptor):
        if descriptor is None:
            return

        coordinates = {
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
                    self.dimensions['shape_height']
            }
        }

        return coordinates[descriptor]

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

    def make_one_shape(self, shape, fill, outline, *args):
        name_create_function = 'create_{}'.format(shape)
        shape = getattr(self.canvas, name_create_function)(
            *args,
            fill=settings.colors[fill],
            outline=settings.colors[outline]
        )

        return shape