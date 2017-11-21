//
// Created by Ivan Pazhitnykh on 9/22/17.
//

#ifndef LAB1_LAB1_H
#define LAB1_LAB1_H

#include <vector>
#include <iostream>
#include <fstream>

#include "omp.h"
#include "utils.h"

using namespace std;

void linear_multiply(matrix_t&, matrix_t&, matrix_t&, int);

void block_multiply(matrix_t&, matrix_t&, matrix_t&, int, int);

#endif //LAB1_LAB1_H
