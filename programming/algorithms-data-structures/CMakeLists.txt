cmake_minimum_required(VERSION 3.3)
project(algorithms)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

# bignum arithmetic
add_executable(big_sum A+B/main.cpp)
add_executable(big_diff A-B/main.cpp)
add_executable(big_mult AxB/main.cpp)
add_executable(big_div A-div-n/main.cpp)

# graph traversals
add_executable(bfs bfs/main.cpp)
add_executable(dfs dfs/main.cpp)

# graph shortest path
add_executable(floyd Floyds/main.cpp)
add_executable(dijkstra Dijkstra's/main.cpp)
add_executable(ford-bellman Ford-Bellman/main.cpp)

# other graphs algorithms
add_executable(bridge_search bridge_searching/main.cpp)
add_executable(cutpoints_search cutpoints_searching/main.cpp)
add_executable(dinic Dinic's/main.cpp)

# data structures
add_executable(list list/main.cpp)
add_executable(stack stack/main.cpp)
add_executable(segment-tree segment-tree/main.cpp)
add_executable(recurrent-segment-tree recurrent-segment-tree/main.cpp)

# substrings search algorithms
add_executable(aho-corasick Aho-Corasick/main.cpp)
add_executable(kmp Knuth-Morris-Pratt/main.cpp)

# other
add_executable(eratosthenes Eratosthenes/main.cpp)
add_executable(brute_force brute_force/main.cpp)
add_executable(cnk C\(n,k\)/main.cpp)
add_executable(comb combination_generating/main.cpp)
add_executable(power power/main.cpp)


