#pragma once
#include <cmath>


auto is_prime(const int num) -> int {
    const auto n {abs(num)};
    if (n == 1) return 0;
    const auto stop { std::ceil(std::sqrt(n+1)) };
    for (auto i {2}; i < stop; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}
