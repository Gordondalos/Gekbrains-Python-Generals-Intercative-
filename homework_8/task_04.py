# Склад оргтехники


class Place:
    def __init__(self, name):
        self.name = name
        self.units = {}

    def __str__(self):
        return (f'{self.name}: {self.units}')

    def add(self, object):
        cnt_cur = self.units.get(object)
        if cnt_cur:
            self.units.update({object: (cnt_cur + 1)})
        else:
            self.units.update({object: 1})

    def transit(self, other, object):
        cnt_from = self.units.get(object)
        self.units.update({object: (cnt_from - 1)})
        cnt_to = other.units.get(object)
        if cnt_to == None:
            cnt_to = 0
        other.units.update({object: (cnt_to + 1)})


class Storage(Place):
    pass


class Office(Place):
    pass


class Equipment:
    def __init__(self, model):
        self.model = model


class Printer(Equipment):
    def __init__(self, model, colorful):
        super().__init__(model)
        self.colorful = colorful


class Scanner(Equipment):
    def __init__(self, model, resolution):
        super().__init__(model)
        self.resolution = resolution


class Copier(Equipment):  # Xerox - это название компании, а не тип техники
    def __init__(self, model, speed):
        super().__init__(model)
        self.speed = speed


office = Office('Офис 1')
office2 = Office('Офис 2')
storage = Storage('Склад')

storage.add('принтер')
storage.add('принтер')
storage.add('сканер')
storage.add('копир')
print(storage)
print(office)
print(office2)

storage.transit(office, 'принтер')
storage.transit(office, 'сканер')
storage.transit(office2, 'копир')
print(storage)
print(office)
print(office2)