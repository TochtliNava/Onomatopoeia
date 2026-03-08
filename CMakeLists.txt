cmake_minimum_required(VERSION 3.15)
project(Onomatopoeia VERSION 0.0.1 LANGUAGES CXX)

add_executable(${PROJECT_NAME}.out src/main.cpp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)