class Engine:
    def __init__(self, power):
        self.power = power

class Transmission:
    def __init__(self, automatic):
        self.automatic = automatic

class Body:
    def __init__(self, color):
        self.color = color
class CarBuilder:
    def __init__(self):
        self.engine = None
        self.transmission = None
        self.body = None

    def set_engine(self, power):
        self.engine = Engine(power)

    def set_transmission(self, automatic):
        self.transmission = Transmission(automatic)

    def set_body(self, color):
        self.body = Body(color)

    def get_car(self):
        return f"Car with Engine: {self.engine.power}, Transmission: {self.transmission.automatic}, Body Color: {self.body.color}"
class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self, power, automatic, color):
        self.builder.set_engine(power)
        self.builder.set_transmission(automatic)
        self.builder.set_body(color)
class SedanBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

class SUVBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

class SportsCarBuilder(CarBuilder):
    def __init__(self):
        super().__init__()
sedan_builder = SedanBuilder()
director = CarDirector(sedan_builder)
director.construct_car("150hp", True, "Red")
sedan = sedan_builder.get_car()
print("Создан седан:", sedan)
