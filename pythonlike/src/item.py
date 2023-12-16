class Item:
    def __init__(self, x: int, y: int, name: str, char: str, color, func=None, **kwargs):
        self.x = x
        self.y = y
        self.name = name
        self.char = char
        self.color = color
        self.func = func
        self.func_kwargs = kwargs
