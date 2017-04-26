//
// Created by Drapegnik on 25.04.17.
//

#ifndef LAB4_GARAGE_H
#define LAB4_GARAGE_H

#include <iostream>
#include "windows.h"
#include <process.h>

#define CHECK(condition) if (!condition) std::cerr

class Garage {
public:
    Garage();

    Garage(int size);

    int getSize() const;

    void freePlace();

    void takePlace();

    void getStatus();

private:
    int size, taked;
};

#endif //LAB4_GARAGE_H
