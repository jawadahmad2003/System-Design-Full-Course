
#include <iostream>
#include <string>
using namespace std;

/*
    POLYMORPHISM IN C++

    Polymorphism means one interface with multiple forms.

    Example:
    - ManualCar accelerates using its own implementation.
    - ElectricCar accelerates using its own implementation.

    The same method name behaves differently
    depending on the object.
*/


// ==================== ABSTRACT PARENT CLASS ====================

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

    // Pure Virtual Function: Must be implemented by child classes
    virtual void accelerate(int speed = 20) = 0;

    // Pure Virtual Function
    virtual void brake() = 0;

    // Virtual Destructor
    virtual ~Car() {}
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

    // Method Overriding: Runtime Polymorphism
    void accelerate(int speed = 20) override {

        if (!isEngineOn) {
            cout << brand << " " << model
                 << " : Cannot accelerate! Engine is off."
                 << endl;
            return;
        }

        currentSpeed += speed;

        cout << brand << " " << model
             << " : Accelerating to "
             << currentSpeed << " km/h" << endl;
    }

    // Method Overriding
    void brake() override {

        currentSpeed -= 20;

        if (currentSpeed < 0) {
            currentSpeed = 0;
        }

        cout << brand << " " << model
             << " : Braking! Speed is now "
             << currentSpeed << " km/h" << endl;
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
             << " : Battery fully charged!" << endl;
    }

    // Method Overriding: Runtime Polymorphism
    void accelerate(int speed = 15) override {

        if (!isEngineOn) {
            cout << brand << " " << model
                 << " : Cannot accelerate! Engine is off."
                 << endl;
            return;
        }

        if (batteryLevel <= 0) {
            cout << brand << " " << model
                 << " : Battery dead! Cannot accelerate."
                 << endl;
            return;
        }

        int batteryUsed = 10 + speed;

        if (batteryUsed > batteryLevel) {
            cout << "Not enough battery!" << endl;
            return;
        }

        batteryLevel -= batteryUsed;
        currentSpeed += speed;

        cout << brand << " " << model
             << " : Accelerating to "
             << currentSpeed << " km/h. "
             << "Battery at " << batteryLevel << "%."
             << endl;
    }

    // Method Overriding
    void brake() override {

        currentSpeed -= 15;

        if (currentSpeed < 0) {
            currentSpeed = 0;
        }

        cout << brand << " " << model
             << " : Regenerative braking! "
             << "Speed is now " << currentSpeed
             << " km/h. "
             << "Battery at " << batteryLevel << "%."
             << endl;
    }
};


// ==================== MAIN PROGRAM ====================

int main() {

    // Parent Class Pointer -> ManualCar Object
    Car* myManualCar = new ManualCar("Ford", "Mustang");

    myManualCar->startEngine();

    myManualCar->accelerate();
    myManualCar->accelerate(40);

    myManualCar->brake();
    myManualCar->stopEngine();

    delete myManualCar;

    cout << "----------------------" << endl;

    // Parent Class Pointer -> ElectricCar Object
    Car* myElectricCar = new ElectricCar("Tesla", "Model S");

    myElectricCar->startEngine();

    myElectricCar->accelerate();
    myElectricCar->accelerate(30);

    myElectricCar->brake();
    myElectricCar->stopEngine();

    delete myElectricCar;

    return 0;
}
