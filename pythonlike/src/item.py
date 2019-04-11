class Item:
    def __init__(self, w, h, name, char, color, func=None, **kwargs):
        self.w = w
        self.h = h
        self.name = name
        self.char = char
        self.color = color
        self.func = func
        self.func_kwargs = kwargs
