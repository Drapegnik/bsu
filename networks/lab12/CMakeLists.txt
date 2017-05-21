cmake_minimum_required(VERSION 3.6)
project(lab12)

set(CMAKE_CXX_STANDARD 11)
set(WIN_SOCK wsock32 ws2_32)

# task1
add_executable(lookup lookup.cpp)
target_link_libraries(lookup ${WIN_SOCK})

# task2
add_executable(mac mac.cpp)
target_link_libraries(mac ${WIN_SOCK} iphlpapi)

# task3
add_executable(tcp-client tcp/client.cpp)
target_link_libraries(tcp-client ${WIN_SOCK})

add_executable(tcp-server tcp/server.cpp)
target_link_libraries(tcp-server ${WIN_SOCK})