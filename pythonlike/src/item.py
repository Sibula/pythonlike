class Item:
    def __init__(self, x, y, name, char, color, func=None, **kwargs):
        self.x = x
        self.y = y
        self.name = name
        self.char = char
        self.color = color
        self.func = func
        self.func_kwargs = kwargs
