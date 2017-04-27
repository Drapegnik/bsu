//
// Created by Drapegnik on 25.04.17.
//

#include "Garage.h"

Garage::Garage() : size(0), taked(0) {}

Garage::Garage(int size) : size(size), taked(0) {
    getStatus();
}

int Garage::getSize() const {
    return size;
}

void Garage::freePlace() {
    taked--;
    getStatus();
}

void Garage::takePlace() {
    taked++;
    getStatus();
}

void Garage::getStatus() {
    std::cout << "(garage): status: [" << taked << "/" << size << "] taked!" << std::endl;
}