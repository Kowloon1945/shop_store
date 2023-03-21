
class Options:
    size_list = ['XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL', '5XL']

class Fut:
    price: int = 1937
    fut = 'Футболка'

class Hud:
    price: int = 4000
    hud = 'Худи'

class FutBel(Options, Fut):
    price: int = Fut.price
    size: str = ''
    name = 'Белая'

    def __init__(self, text_size):
        if text_size in Options.size_list:
            self.size = text_size
            self.name = Fut.fut + ' ' + self.name
        else:
            raise Exception('Неправильно указан размер')


x = FutBel('XL')
print(x.name, x.size)

class FutRed(Options, Fut):
    price: int = Fut.price
    size: str = ''
    name = 'Красная'

    def __init__(self, text_size):
        if text_size in Options.size_list:
            self.size = text_size
            self.name = Fut.fut + ' ' + self.name
        else:
            raise Exception('Неправильно указан размер')
y = FutRed('S')
print(y.name, y.size)

class FutBlack(Options, Fut):
    price: int = Fut.price
    size: str = ''
    name = 'Черная'

    def __init__(self, text_size):
        if text_size in Options.size_list:
            self.size = text_size
            self.name = Fut.fut + ' ' + self.name
        else:
            raise Exception('Неправильно указан размер')
z = FutBlack('S')
z1 = FutBlack('XS')
print(z.name, z.size)
print(z1.name, z1.size)


class HudBlue(Options, Hud):
    price: int = Hud.price
    size: str = ''
    name = 'Голубая'

    def __init__(self, text_size):
        if text_size in Options.size_list:
            self.size = text_size
            self.name = Fut.fut + ' ' + self.name
        else:
            raise Exception('Неправильно указан размер')


class HudOrange(Options, Hud):
    price: int = Hud.price
    size: str = ''
    name = 'Оранжевая'

    def __init__(self, text_size):
        if text_size in Options.size_list:
            self.size = text_size
            self.name = Fut.fut + ' ' + self.name
        else:
            raise Exception('Неправильно указан размер')

















