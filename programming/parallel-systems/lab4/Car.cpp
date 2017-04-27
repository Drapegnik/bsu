//
// Created by Drapegnik on 25.04.17.
//

#include "Car.h"

Car::Car(int id) : id(id), inGarage(false), numLeave(0), numEnter(0) {}

bool Car::isInGarage() const {
    return inGarage;
}

void Car::leaveGarage() {
    Sleep(rand() % 5000);
    numLeave++;
    std::cout << "(car#" << id << "): LEAVE" << std::endl;
    inGarage = false;
}

void Car::enterGarage() {
    Sleep(rand() % 5000);
    numEnter++;
    std::cout << "(car#" << id << "): ENTER" << std::endl;
    inGarage = true;
}

void Car::getInfo() {
    std::cout << "(car#" << id << "): enters - " << numEnter << ", leaves - " << numLeave << std::endl;
}