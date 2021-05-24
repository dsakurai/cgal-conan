cmake_minimum_required(VERSION 3.17)

project(test_cgal)

set(CMAKE_CXX_STANDARD 20)

set(CONAN_DISABLE_CHECK_COMPILER Yes)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)


add_executable(test_boolean_operations boolean_operations.cpp)

add_executable(test_arrangement_with_history arrangement_with_history.cpp)

foreach(target IN ITEMS test_boolean_operations test_arrangement_with_history)
    target_link_libraries(${target}
            ${CONAN_LIBS}
            )
endforeach()
