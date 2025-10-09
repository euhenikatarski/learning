class Car:

    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}".title()
        return long_name.title()

    def read_odometer(self):
        print(f"Этот автомобиль имеет пробег {self.odometer_reading} км.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Нельзя откатить одометр назад!")

    def increment_odometer(self, km):
        self.odometer_reading += km


class Battery:

    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Этот автомобиль имеет аккумулятор {self.battery_size}-кВт·ч.")

    def get_range(self):
        if self.battery_size == 75:
            range_km = 260
        elif self.battery_size == 100:
            range_km = 315
        elif self.battery_size == 65:
            range_km = 225
        print(f"Запас хода этого авто примерно {range_km} км.")

    def upgrade_battery(self, battery_power=65):
        self.battery_size = battery_power


class ElectricCar(Car):

    """Представляет аспекты, специфичные для электромобилей."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()   # экземпляр Battery как атрибут

car = ElectricCar('honda','civic','2005')
print(car.get_descriptive_name())
car.battery.describe_battery()
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.describe_battery()
car.battery.get_range()