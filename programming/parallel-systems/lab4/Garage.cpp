//
// Created by Drapegnik on 25.04.17.
//

#include "Garage.h"

Garage::Garage() : size(0), free(0) {}

Garage::Garage(int size) : size(size), free(free) {}

int Garage::getSize() const {
    return size;
}

void Garage::freePlace() {
    free++;
    getInfo();
}

void Garage::takePlace() {
    free--;
    getInfo();
}

void Garage::getInfo() {
    std::cout << "(garage): number of free places: " << free << "/" << size << std::endl;
}