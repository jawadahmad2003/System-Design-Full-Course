
"""
POLYMORPHISM IN PYTHON

Polymorphism means one interface with multiple forms.

Example:
- ManualCar accelerates using its own implementation.
- ElectricCar accelerates using its own implementation.

The same method name behaves differently
depending on the object.
"""

from abc import ABC, abstractmethod


# ==================== ABSTRACT PARENT CLASS ====================

class Car(ABC):

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

    # Abstract Method: Must be implemented by child classes
    @abstractmethod
    def accelerate(self, speed=20):
        pass

    # Abstract Method
    @abstractmethod
    def brake(self):
        pass


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

    # Method Overriding: Runtime Polymorphism
    def accelerate(self, speed=20):

        if not self._is_engine_on:
            print(
                f"{self._brand} {self._model} : "
                "Cannot accelerate! Engine is off."
            )
            return

        self._current_speed += speed

        print(
            f"{self._brand} {self._model} : "
            f"Accelerating to {self._current_speed} km/h"
        )

    # Method Overriding
    def brake(self):

        self._current_speed -= 20

        if self._current_speed < 0:
            self._current_speed = 0

        print(
            f"{self._brand} {self._model} : "
            f"Braking! Speed is now {self._current_speed} km/h"
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

    # Method Overriding: Runtime Polymorphism
    def accelerate(self, speed=15):

        if not self._is_engine_on:
            print(
                f"{self._brand} {self._model} : "
                "Cannot accelerate! Engine is off."
            )
            return

        if self.__battery_level <= 0:
            print(
                f"{self._brand} {self._model} : "
                "Battery dead! Cannot accelerate."
            )
            return

        battery_used = 10 + speed

        if battery_used > self.__battery_level:
            print("Not enough battery!")
            return

        self.__battery_level -= battery_used
        self._current_speed += speed

        print(
            f"{self._brand} {self._model} : "
            f"Accelerating to {self._current_speed} km/h. "
            f"Battery at {self.__battery_level}%."
        )

    # Method Overriding
    def brake(self):

        self._current_speed -= 15

        if self._current_speed < 0:
            self._current_speed = 0

        print(
            f"{self._brand} {self._model} : "
            f"Regenerative braking! "
            f"Speed is now {self._current_speed} km/h. "
            f"Battery at {self.__battery_level}%."
        )


# ==================== MAIN PROGRAM ====================

# Parent Class Reference -> ManualCar Object
my_manual_car = ManualCar("Ford", "Mustang")

my_manual_car.start_engine()

my_manual_car.accelerate()
my_manual_car.accelerate(40)

my_manual_car.brake()
my_manual_car.stop_engine()

print("----------------------")

# Parent Class Reference -> ElectricCar Object
my_electric_car = ElectricCar("Tesla", "Model S")

my_electric_car.start_engine()

my_electric_car.accelerate()
my_electric_car.accelerate(30)

my_electric_car.brake()
my_electric_car.stop_engine()
