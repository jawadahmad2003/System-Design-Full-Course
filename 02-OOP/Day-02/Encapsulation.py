
"""
ENCAPSULATION IN PYTHON

Encapsulation explains two things:

1. An object's characteristics (attributes) and
   behaviours (methods) are encapsulated together
   within that object.

2. All characteristics and behaviours should not be
   directly accessible to everyone.

   Objects should provide controlled access to data.

We implement encapsulation by:

1. Creating a class that acts as a blueprint for objects.
   The class contains attributes and methods together.

2. Using access conventions and properties to control
   access to class attributes.

Example:
SportsCar represents a real-world sports car.
"""


# ==================== SPORTS CAR CLASS ====================

class SportsCar:

    def __init__(self, brand, model):

        # Private Attributes (Name Mangling)
        self.__brand = brand
        self.__model = model
        self.__is_engine_on = False
        self.__current_speed = 0
        self.__current_gear = 0

        # Variable to demonstrate Getters and Setters
        self.__tyre_company = "MRF"

    # ==================== GETTERS ====================

    def get_speed(self):
        return self.__current_speed

    def get_tyre_company(self):
        return self.__tyre_company

    # ==================== SETTER ====================

    def set_tyre_company(self, tyre_company):
        self.__tyre_company = tyre_company

    # ==================== CAR METHODS ====================

    def start_engine(self):

        self.__is_engine_on = True

        print(
            f"{self.__brand} {self.__model} : "
            "Engine starts with a roar!"
        )

    def shift_gear(self, gear):

        if not self.__is_engine_on:
            print(
                f"{self.__brand} {self.__model} : "
                "Engine is off! Cannot Shift Gear."
            )
            return

        self.__current_gear = gear

        print(
            f"{self.__brand} {self.__model} : "
            f"Shifted to gear {self.__current_gear}"
        )

    def accelerate(self):

        if not self.__is_engine_on:
            print(
                f"{self.__brand} {self.__model} : "
                "Engine is off! Cannot accelerate."
            )
            return

        self.__current_speed += 20

        print(
            f"{self.__brand} {self.__model} : "
            f"Accelerating to {self.__current_speed} km/h"
        )

    def brake(self):

        self.__current_speed -= 20

        if self.__current_speed < 0:
            self.__current_speed = 0

        print(
            f"{self.__brand} {self.__model} : "
            f"Braking! Speed is now {self.__current_speed} km/h"
        )

    def stop_engine(self):

        self.__is_engine_on = False
        self.__current_gear = 0
        self.__current_speed = 0

        print(
            f"{self.__brand} {self.__model} : "
            "Engine turned off."
        )


# ==================== MAIN PROGRAM ====================

# Creating SportsCar Object
my_sports_car = SportsCar("Ford", "Mustang")

my_sports_car.start_engine()
my_sports_car.shift_gear(1)
my_sports_car.accelerate()
my_sports_car.shift_gear(2)
my_sports_car.accelerate()
my_sports_car.brake()
my_sports_car.stop_engine()

# Direct access is discouraged:
# my_sports_car.__current_speed = 500

# Accessing private data through Getter
print(
    "Current Speed of My Sports Car is",
    my_sports_car.get_speed()
)

# Accessing tyre company through Getter
print(
    "Tyre Company:",
    my_sports_car.get_tyre_company()
)

# Updating tyre company through Setter
my_sports_car.set_tyre_company("Michelin")

print(
    "Updated Tyre Company:",
    my_sports_car.get_tyre_company()
)
