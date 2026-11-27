
"""
INHERITANCE IN PYTHON

A child class inherits properties and methods
from its parent class.

Example:
- Car is the Parent Class.
- ManualCar is a Child Class.
- ElectricCar is a Child Class.

Both child classes reuse common properties and
methods from the Car class.
"""


# ==================== PARENT CLASS ====================

class Car:

    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        self._is_engine_on = False
        self._current_speed = 0

    # Common method: Start Engine
    def start_engine(self):
        self._is_engine_on = True

        print(f"{self._brand} {self._model} : Engine started.")

    # Common method: Stop Engine
    def stop_engine(self):
        self._is_engine_on = False
        self._current_speed = 0

        print(f"{self._brand} {self._model} : Engine turned off.")

    # Common method: Accelerate
    def accelerate(self):

        if not self._is_engine_on:
            print(
                f"{self._brand} {self._model} : "
                "Cannot accelerate! Engine is off."
            )
            return

        self._current_speed += 20

        print(
            f"{self._brand} {self._model} : "
            f"Accelerating to {self._current_speed} km/h"
        )

    # Common method: Brake
    def brake(self):

        self._current_speed -= 20

        if self._current_speed < 0:
            self._current_speed = 0

        print(
            f"{self._brand} {self._model} : "
            f"Braking! Speed is now {self._current_speed} km/h"
        )


# ==================== CHILD CLASS 1 ====================

class ManualCar(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)

        self.__current_gear = 0

    # Specific method for Manual Car
    def shift_gear(self, gear):

        self.__current_gear = gear

        print(
            f"{self._brand} {self._model} : "
            f"Shifted to gear {self.__current_gear}"
        )


# ==================== CHILD CLASS 2 ====================

class ElectricCar(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)

        self.__battery_level = 100

    # Specific method for Electric Car
    def charge_battery(self):

        self.__battery_level = 100

        print(
            f"{self._brand} {self._model} : "
            "Battery fully charged!"
        )


# ==================== MAIN FUNCTION ====================

# Manual Car Object
my_manual_car = ManualCar("Suzuki", "WagonR")

my_manual_car.start_engine()
my_manual_car.shift_gear(1)
my_manual_car.accelerate()
my_manual_car.brake()
my_manual_car.stop_engine()

print("----------------------")

# Electric Car Object
my_electric_car = ElectricCar("Tesla", "Model S")

my_electric_car.charge_battery()
my_electric_car.start_engine()
my_electric_car.accelerate()
my_electric_car.brake()
my_electric_car.stop_engine()
