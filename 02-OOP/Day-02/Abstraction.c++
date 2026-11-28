
#include <iostream>
#include <string>

using namespace std;

/*
ABSTRACTION IN C++

Abstract Class:

1. Acts as an interface for the outside world to operate the car.

2. Tells WHAT a car can do rather than HOW it does it.

3. We cannot directly create objects of an abstract class.

4. Child classes inherit the abstract class and must provide
   implementations for all pure virtual functions.

REAL-WORLD EXAMPLE:

Imagine sitting inside a car.

You can operate the car using:
- Start button
- Accelerator pedal
- Brake pedal
- Gear lever

You do not need to know the internal implementation
of these operations.

The abstract class Car defines WHAT operations are available.

The concrete class SportsCar defines HOW they work.
*/


// ==================== ABSTRACT PARENT CLASS ====================

class Car {

public:

    // Pure Virtual Functions

    virtual void startEngine() = 0;

    virtual void shiftGear(int gear) = 0;

    virtual void accelerate() = 0;

    virtual void brake() = 0;

    virtual void stopEngine() = 0;

    // Virtual Destructor
    virtual ~Car() {}
};


// ==================== CONCRETE CHILD CLASS ====================

/*
SportsCar is a Concrete Class.

A concrete class provides implementation details
for all pure virtual functions of its parent class.

It can be instantiated after implementing all
inherited pure virtual functions.
*/


class SportsCar : public Car {

public:

    string brand;
    string model;
    bool isEngineOn;
    int currentSpeed;
    int currentGear;

    // Constructor
    SportsCar(string b, string m) {

        this->brand = b;
        this->model = m;
        isEngineOn = false;
        currentSpeed = 0;
        currentGear = 0;
    }

    // ==================== METHOD IMPLEMENTATIONS ====================

    void startEngine() override {

        isEngineOn = true;

        cout << brand << " " << model
             << " : Engine starts with a roar!" << endl;
    }

    void shiftGear(int gear) override {

        if (!isEngineOn) {
            cout << brand << " " << model
                 << " : Engine is off! Cannot Shift Gear."
                 << endl;
            return;
        }

        currentGear = gear;

        cout << brand << " " << model
             << " : Shifted to gear "
             << currentGear << endl;
    }

    void accelerate() override {

        if (!isEngineOn) {
            cout << brand << " " << model
                 << " : Engine is off! Cannot accelerate."
                 << endl;
            return;
        }

        currentSpeed += 20;

        cout << brand << " " << model
             << " : Accelerating to "
             << currentSpeed << " km/h" << endl;
    }

    void brake() override {

        currentSpeed -= 20;

        if (currentSpeed < 0)
            currentSpeed = 0;

        cout << brand << " " << model
             << " : Braking! Speed is now "
             << currentSpeed << " km/h" << endl;
    }

    void stopEngine() override {

        isEngineOn = false;
        currentGear = 0;
        currentSpeed = 0;

        cout << brand << " " << model
             << " : Engine turned off." << endl;
    }
};


// ==================== MAIN FUNCTION ====================

int main() {

    // Abstract Class Pointer -> Concrete Class Object
    Car* myCar = new SportsCar("Ford", "Mustang");

    myCar->startEngine();
    myCar->shiftGear(1);
    myCar->accelerate();
    myCar->shiftGear(2);
    myCar->accelerate();
    myCar->brake();
    myCar->stopEngine();

    // Memory Cleanup
    delete myCar;

    return 0;
}
