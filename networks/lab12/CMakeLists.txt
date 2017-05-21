cmake_minimum_required(VERSION 3.6)
project(lab12)

set(CMAKE_CXX_STANDARD 11)
set(WIN_SOCK wsock32 ws2_32)

add_executable(lookup lookup.cpp)
target_link_libraries(lookup ${WIN_SOCK})

add_executable(mac mac.cpp)
target_link_libraries(mac ${WIN_SOCK} iphlpapi)