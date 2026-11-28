
#include <iostream>
#include <string>

using namespace std;

/*
ENCAPSULATION IN C++

Encapsulation explains two things:

1. An object's characteristics (variables) and behaviours
   (methods) are encapsulated together within that object.

2. All characteristics and behaviours should not be
   directly accessible to everyone.

We implement encapsulation using:

1. Classes to combine data and methods.
2. Access modifiers (private, public, protected)
   to control access to class members.
3. Getters and Setters for controlled data access.
*/


// ==================== SPORTS CAR CLASS ====================

class SportsCar {

private:
    // Private Attributes
    string brand;
    string model;
    bool isEngineOn;
    int currentSpeed;
    int currentGear;

    // Variable to demonstrate Getters and Setters
    string tyreCompany;

public:

    // Constructor
    SportsCar(string b, string m) {

        this->brand = b;
        this->model = m;
        isEngineOn = false;
        currentSpeed = 0;
        currentGear = 0;
        tyreCompany = "MRF";
    }

    // ==================== GETTERS ====================

    int getSpeed() {
        return currentSpeed;
    }

    string getTyreCompany() {
        return tyreCompany;
    }

    // ==================== SETTER ====================

    void setTyreCompany(string tyreCompany) {
        this->tyreCompany = tyreCompany;
    }

    // ==================== CAR METHODS ====================

    void startEngine() {

        isEngineOn = true;

        cout << brand << " " << model
             << " : Engine starts with a roar!" << endl;
    }

    void shiftGear(int gear) {

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

    void accelerate() {

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

    void brake() {

        currentSpeed -= 20;

        if (currentSpeed < 0)
            currentSpeed = 0;

        cout << brand << " " << model
             << " : Braking! Speed is now "
             << currentSpeed << " km/h" << endl;
    }

    void stopEngine() {

        isEngineOn = false;
        currentGear = 0;
        currentSpeed = 0;

        cout << brand << " " << model
             << " : Engine turned off." << endl;
    }

    // Destructor
    ~SportsCar() {}
};


// ==================== MAIN FUNCTION ====================

int main() {

    // Creating SportsCar Object
    SportsCar* mySportsCar =
        new SportsCar("Ford", "Mustang");

    mySportsCar->startEngine();
    mySportsCar->shiftGear(1);
    mySportsCar->accelerate();
    mySportsCar->shiftGear(2);
    mySportsCar->accelerate();
    mySportsCar->brake();
    mySportsCar->stopEngine();

    // Direct access is not allowed:
    // mySportsCar->currentSpeed = 500;

    // Accessing private data using Getter
    cout << "Current Speed of My Sports Car is "
         << mySportsCar->getSpeed() << endl;

    // Accessing tyre company using Getter
    cout << "Tyre Company: "
         << mySportsCar->getTyreCompany() << endl;

    // Updating tyre company using Setter
    mySportsCar->setTyreCompany("Michelin");

    cout << "Updated Tyre Company: "
         << mySportsCar->getTyreCompany() << endl;

    // Memory Cleanup
    delete mySportsCar;

    return 0;
}
