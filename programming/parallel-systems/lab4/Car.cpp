//
// Created by Drapegnik on 25.04.17.
//

#include "Car.h"

Car::Car(int id) : id(id), inGarage(false), numLeave(0), numEnter(0) {}

bool Car::isInGarage() const {
    return inGarage;
}

void Car::leaveGarage() {
    numLeave++;
    std::cout << "(car#" << id << "): leave Garage" << std::endl;
    inGarage = false;
}

void Car::enterGarage() {
    numEnter++;
    std::cout << "(car#" << id << "): enter Garage" << std::endl;
    inGarage = true;
}

void Car::getInfo() {
    std::cout << "(car#" << id << "): enter - " << numEnter << ", leave - " << numLeave << std::endl;
}