import abc


class ComputerColor(abc.ABC):

    @abc.abstractmethod
    def __repr__(self):
        return

    @abc.abstractmethod
    def __mul__(self, c):
        return

    @abc.abstractmethod
    def __rmul__(self, c):
        return


class Color(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red, green, blue):
        self.red = red
        self.blue = blue
        self.green = green

    # def __str__(self):
    #     return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'

    def __repr__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, other):
        if self.red == other.red and self.green == other.green and self.blue == other.blue:
            return True
        else:
            return False
        # return self.__str__() == other.__str__()

    def __add__(self, other):
        # new = Color((self.red + other.red) // 2, (self.green + other.green) // 2, (self.blue + other.blue) // 2)
        new = Color((self.red + other.red), (self.green + other.green), (self.blue + other.blue))
        return new

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, c):
        if c < 0 or c > 1:
            raise ValueError('Contrast coefficient must be between 0 and 1')
        else:
            contrast_level = -256*(1-c)
            F = 259 * (contrast_level + 255)/(255*(259-contrast_level))
            L_red_new = int(F * (self.red - 128) + 128)
            L_green_new = int(F * (self.green - 128) + 128)
            L_blue_new = int(F * (self.blue - 128) + 128)
        return Color(L_red_new, L_green_new, L_blue_new)

    def __rmul__(self, c):
        return self.__mul__(c)


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]

    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    red = Color(255, 0, 0)
    red1 = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red)
    print(green)
    print(red == green)
    print(red == Color(255, 0, 0))
    print(red + green)

    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(set(color_list))
    print(red * 0.5)
    print(0.5 * orange1)
    print_a(orange1)
