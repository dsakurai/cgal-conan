cmake_minimum_required(VERSION 3.17)

project(test_cgal)

set(CMAKE_CXX_STANDARD 20)

set(CONAN_DISABLE_CHECK_COMPILER Yes)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)

add_executable(test_cgal main.cpp)

target_link_libraries(test_cgal
        ${CONAN_LIBS}
        )
