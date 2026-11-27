
#include <iostream>
#include <string>
using namespace std;

/*
    INHERITANCE IN C++

    A child class inherits properties and methods
    from its parent class.

    Example:
    - Car is the Parent Class.
    - ManualCar is a Child Class.
    - ElectricCar is a Child Class.

    Both child classes reuse common properties
    and methods from the Car class.
*/


// ==================== PARENT CLASS ====================

class Car {
protected:
    string brand;
    string model;
    bool isEngineOn;
    int currentSpeed;

public:

    // Constructor
    Car(string brand, string model) {
        this->brand = brand;
        this->model = model;
        this->isEngineOn = false;
        this->currentSpeed = 0;
    }

    // Common method: Start Engine
    void startEngine() {
        isEngineOn = true;

        cout << brand << " " << model
             << " : Engine started." << endl;
    }

    // Common method: Stop Engine
    void stopEngine() {
        isEngineOn = false;
        currentSpeed = 0;

        cout << brand << " " << model
             << " : Engine turned off." << endl;
    }

    // Common method: Accelerate
    void accelerate() {

        if (!isEngineOn) {
            cout << brand << " " << model
                 << " : Cannot accelerate! Engine is off."
                 << endl;
            return;
        }

        currentSpeed += 20;

        cout << brand << " " << model
             << " : Accelerating to "
             << currentSpeed << " km/h" << endl;
    }

    // Common method: Brake
    void brake() {

        currentSpeed -= 20;

        if (currentSpeed < 0) {
            currentSpeed = 0;
        }

        cout << brand << " " << model
             << " : Braking! Speed is now "
             << currentSpeed << " km/h" << endl;
    }
};


// ==================== CHILD CLASS 1 ====================

class ManualCar : public Car {

private:
    int currentGear;

public:

    // Constructor
    ManualCar(string brand, string model)
        : Car(brand, model) {

        currentGear = 0;
    }

    // Specific method for Manual Car
    void shiftGear(int gear) {

        currentGear = gear;

        cout << brand << " " << model
             << " : Shifted to gear "
             << currentGear << endl;
    }
};


// ==================== CHILD CLASS 2 ====================

class ElectricCar : public Car {

private:
    int batteryLevel;

public:

    // Constructor
    ElectricCar(string brand, string model)
        : Car(brand, model) {

        batteryLevel = 100;
    }

    // Specific method for Electric Car
    void chargeBattery() {

        batteryLevel = 100;

        cout << brand << " " << model
             << " : Battery fully charged!"
             << endl;
    }
};


// ==================== MAIN FUNCTION ====================

int main() {

    // Manual Car Object
    ManualCar myManualCar("Suzuki", "WagonR");

    myManualCar.startEngine();
    myManualCar.shiftGear(1);
    myManualCar.accelerate();
    myManualCar.brake();
    myManualCar.stopEngine();

    cout << "----------------------" << endl;

    // Electric Car Object
    ElectricCar myElectricCar("Tesla", "Model S");

    myElectricCar.chargeBattery();
    myElectricCar.startEngine();
    myElectricCar.accelerate();
    myElectricCar.brake();
    myElectricCar.stopEngine();

    return 0;
}
