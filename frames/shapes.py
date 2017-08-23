import tkinter as tk

from settings import settings


class ShapesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(padx=40)

        # set values for canvas_width, canvas_height, shape_number,
        # shape_width, shape_height, all in pixels
        self.dimensions = self.set_dimensions(600, 200, 4, 100, 100)

        self.canvas = self.make_canvas()
        self.canvas.grid()

        # initialize shape features of shape, fill, outline, and descriptor
        # for coordinates required to draw shape
        self.shape_features = self.set_shape_features(None, None, None, None)
        self.current_shapes = []

        # draw shape_number of shapes
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

    def set_shape_features(self, shape, fill, outline, coordinates_descriptor):
        features = {
            'shape': shape,
            'fill': fill,
            'outline': outline,
            'coordinates_descriptor': coordinates_descriptor
        }
        return features

    # based on dimensions and coordinates descriptor, get actual coordinates
    # required for shape
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

    # draw one shape when called by make_shapes method
    def make_one_shape(self, shape, fill, outline, *args):
        name_create_function = 'create_{}'.format(shape)
        shape = getattr(self.canvas, name_create_function)(
            *args,
            fill=settings.colors[fill],
            outline=settings.colors[outline]
        )

        return shape

    # iterate over shape_number of coordinates and draw shapes
    def make_shapes(self, shape, fill, outline, coordinates_descriptor):
        for current_shape in self.current_shapes:
            self.canvas.delete(current_shape)

        self.set_shape_features(shape, fill, outline, coordinates_descriptor)

        self.current_shapes = []

        for i in range(0, self.dimensions['shape_number']):
            self.current_shapes.append(
                self.make_one_shape(
                    shape, fill, outline,
                    list(
                        self.get_coordinates(
                            i, coordinates_descriptor)
                        .values())))
