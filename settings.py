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

    # add standard configuration for buttons
    def button_standard_config(self, button):
        button.configure(padx=15, pady=5)


settings = Settings()
