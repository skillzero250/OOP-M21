from abc import ABC, abstractmethod


# Абстрактная фабрика для создания различных типов автомобилей
class CarFactory(ABC):
    @abstractmethod
    def produce_car(self):
        pass


# Конкретная реализация абстрактной фабрики для электрического автомобиля
class ElectricCarFactory(CarFactory):
    def produce_car(self):
        return ElectricCar()


# Конкретная реализация абстрактной фабрики для бензинового автомобиля
class PetrolCarFactory(CarFactory):
    def produce_car(self):
        return PetrolCar()


# Конкретная реализация абстрактной фабрики для гибридного автомобиля
class HybridCarFactory(CarFactory):
    def produce_car(self):
        return HybridCar()


# Абстрактный класс Car
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass


# Конкретные классы для каждого типа автомобилей
class ElectricCar(Car):
    def drive(self):
        print("Driving an electric car.")


class PetrolCar(Car):
    def drive(self):
        print("Driving a petrol car.")


class HybridCar(Car):
    def drive(self):
        print("Driving a hybrid car.")


# Использование абстрактной фабрики для создания экземпляров различных типов автомобилей
electric_factory = ElectricCarFactory()
petrol_factory = PetrolCarFactory()
hybrid_factory = HybridCarFactory()

electric_car = electric_factory.produce_car()
petrol_car = petrol_factory.produce_car()
hybrid_car = hybrid_factory.produce_car()

electric_car.drive()
petrol_car.drive()
hybrid_car.drive()
