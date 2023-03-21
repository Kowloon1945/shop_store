
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


x = FutUch('XL')
print(x.name, x.size)

class FutPent(Options, Fut):
    price: int = Fut.price
    size: str = ''
    name = 'Пентаграмма'

    def __init__(self, text_size):
        if text_size in Options.size_list:
            self.size = text_size
            self.name = Fut.fut + ' ' + self.name
        else:
            raise Exception('Неправильно указан размер')
y = FutPent('S')
print(y.name, y.size)

class FutStal(Options, Fut):
    price: int = Fut.price
    size: str = ''
    name = 'Сталинеш'

    def __init__(self, text_size):
        if text_size in Options.size_list:
            self.size = text_size
            self.name = Fut.fut + ' ' + self.name
        else:
            raise Exception('Неправильно указан размер')
z = FutStal('S')
z1 = FutStal('XS')
print(z.name, z.size)
print(z1.name, z1.size)


class HudUch(Options, Hud):
    price: int = Hud.price
    size: str = ''
    name = 'Учение'

    def __init__(self, text_size):
        if text_size in Options.size_list:
            self.size = text_size
            self.name = Fut.fut + ' ' + self.name
        else:
            raise Exception('Неправильно указан размер')


class HudPent(Options, Hud):
    price: int = Hud.price
    size: str = ''
    name = 'Пентаграмма'

    def __init__(self, text_size):
        if text_size in Options.size_list:
            self.size = text_size
            self.name = Fut.fut + ' ' + self.name
        else:
            raise Exception('Неправильно указан размер')

















