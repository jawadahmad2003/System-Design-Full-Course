
"""
ABSTRACTION IN PYTHON

Abstract Class:

1. Acts as an interface for the outside world to operate
   the car.

2. Tells WHAT a car can do rather than HOW it does it.

3. We cannot directly create objects of an abstract class.

4. Child classes inherit the abstract class and must
   implement all its abstract methods.

REAL-WORLD EXAMPLE:

Imagine sitting inside a car.

You can operate the car using:
- Start button
- Accelerator pedal
- Brake pedal
- Gear lever

You do not need to know the internal implementation
of these operations.

The abstract class Car defines WHAT operations
are available.

The concrete class SportsCar defines HOW they work.
"""


from abc import ABC, abstractmethod


# ==================== ABSTRACT PARENT CLASS ====================

class Car(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def shift_gear(self, gear):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


# ==================== CONCRETE CHILD CLASS ====================

"""
SportsCar is a Concrete Class.

A concrete class provides implementation details
for all abstract methods of its parent class.

It can be instantiated after implementing all
inherited abstract methods.
"""


class SportsCar(Car):

    def __init__(self, brand, model):

        self.brand = brand
        self.model = model
        self.is_engine_on = False
        self.current_speed = 0
        self.current_gear = 0

    # ==================== METHOD IMPLEMENTATIONS ====================

    def start_engine(self):

        self.is_engine_on = True

        print(
            f"{self.brand} {self.model} : "
            "Engine starts with a roar!"
        )

    def shift_gear(self, gear):

        if not self.is_engine_on:
            print(
                f"{self.brand} {self.model} : "
                "Engine is off! Cannot Shift Gear."
            )
            return

        self.current_gear = gear

        print(
            f"{self.brand} {self.model} : "
            f"Shifted to gear {self.current_gear}"
        )

    def accelerate(self):

        if not self.is_engine_on:
            print(
                f"{self.brand} {self.model} : "
                "Engine is off! Cannot accelerate."
            )
            return

        self.current_speed += 20

        print(
            f"{self.brand} {self.model} : "
            f"Accelerating to {self.current_speed} km/h"
        )

    def brake(self):

        self.current_speed -= 20

        if self.current_speed < 0:
            self.current_speed = 0

        print(
            f"{self.brand} {self.model} : "
            f"Braking! Speed is now {self.current_speed} km/h"
        )

    def stop_engine(self):

        self.is_engine_on = False
        self.current_gear = 0
        self.current_speed = 0

        print(
            f"{self.brand} {self.model} : "
            "Engine turned off."
        )


# ==================== MAIN PROGRAM ====================

# Abstract Class Reference -> Concrete Class Object
my_car = SportsCar("Ford", "Mustang")

my_car.start_engine()
my_car.shift_gear(1)
my_car.accelerate()
my_car.shift_gear(2)
my_car.accelerate()
my_car.brake()
my_car.stop_engine()
