RED = ['#FF%02X%02X' % (color, color) for color in range(255, 0, -1)]
GREEN = ['#%02XFF%02X' % (color, color) for color in range(255, 0, -1)]
BLUE = ['#%02X%02XFF' % (color, color) for color in range(255, 0, -1)]
# GRAY = ['#6C6C6C' if color < 108: '#6C6C6C' else '#%02X%02X%02X' % (color, color, color) for color in range(255, 0, -1)]
GRAY = []

for color in range(0, 255):
    if color < 108:
        GRAY.append('#6C6C6C')
    elif color < 150:
        GRAY.append('#%02X%02X%02X' % (color, color, color))
    else:
        GRAY.append('#%02X%02X%02X' % (150, 150, 150))

print(GRAY)


# [f(x) if x is not None else '' for x in xs]

class ColorRange:
    CURRENT = -1
    MOD = True
    colors = {
        "RED": RED,
        "GREEN": GREEN,
        "BLUE": BLUE,
        "GRAY": GRAY,
    }

    def __init__(self, color: list, background: str):
        self.color = color
        self.color[0] = background

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
