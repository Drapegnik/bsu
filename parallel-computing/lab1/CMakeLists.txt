cmake_minimum_required(VERSION 3.7)
project(lab1)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_COMPILER /usr/local/bin/g++-7)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp -m64")

set(SOURCE_FILES lab1.cpp lab1.h utils.cpp utils.h)
add_executable(lab1 ${SOURCE_FILES})