class ColorRange:
    CURRENT = -1
    MOD = True

    def __init__(self, color: list):
        self.color = color
        self.color[0] = "#F8F5F5"

    def __iter__(self):
        if self.MOD:
            self.CURRENT = -1
        else:
            self.CURRENT = 255
        return self

    def __next__(self):
        if self.MOD:
            self.CURRENT += 1
        else:
            self.CURRENT -= 1

        try:
            return self.color[self.CURRENT]
        except IndexError:
            raise StopIteration

    def change_mod(self, mod: bool) -> None:
        self.MOD = mod

    def get_color(self, index: int) -> str:
        return self.color[index]


RED = ['#FF%02X%02X' % (color, color) for color in range(255, 0, -1)]
GREEN = ['#%02XFF%02X' % (color, color) for color in range(255, 0, -1)]
BLUE = ['#%02X%02XFF' % (color, color) for color in range(255, 0, -1)]
