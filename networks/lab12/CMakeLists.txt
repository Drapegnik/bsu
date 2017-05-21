cmake_minimum_required(VERSION 3.6)
project(lab12)

set(CMAKE_CXX_STANDARD 11)

add_executable(lookup lookup.cpp)
target_link_libraries(lookup wsock32 ws2_32)