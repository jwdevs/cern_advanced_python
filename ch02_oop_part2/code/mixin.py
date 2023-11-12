class Animal:
    def __init__(self, name):
        self.name = name


class CanSwim:
    def swim(self):
        print(f'{self.name} swims')


class CanFly:
    def fly(self):
        print(f'{self.name} flies')


class Bird(Animal, CanFly):
    ...


class FlyingFish(Animal, CanFly, CanSwim):
    ...


sky_glider = FlyingFish('SkyGlider')
sky_glider.fly()   # SkyGlider flies
sky_glider.swim()  # SkyGlider swims
