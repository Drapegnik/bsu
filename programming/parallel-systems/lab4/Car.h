//
// Created by Drapegnik on 25.04.17.
//

#ifndef LAB4_CAR_H
#define LAB4_CAR_H

#include <windows.h>
#include <process.h>
#include <iostream>

class Car {
public:
    Car(int id);

    bool isInGarage() const;

    void leaveGarage();

    void enterGarage();

    void getInfo();
private:
    int id, numEnter, numLeave;
    bool inGarage;
};


#endif //LAB4_CAR_H
