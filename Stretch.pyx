#!python3
#distutils: language = c++


cdef extern from "Stretch.hpp":
    int _is_prime "is_prime"(int)


def is_prime(num: int) -> bool:
    return _is_prime(num) == 1
