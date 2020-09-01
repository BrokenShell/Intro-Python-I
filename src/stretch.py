"""
## Stretch Goals

1. One of Python's main philosophical tenets is its emphasis on readability. To
   that end, the Python community has standardized around a style guide called
   [PEP 8](https://www.python.org/dev/peps/pep-0008/). Take a look at it and
   then go over the code you've written and make sure it adheres to what PEP 8
   recommends. Alternatively, PEP 8 linters exist for most code editors (you can
   find instructions on installing a Python linter for VSCode
   [here](https://code.visualstudio.com/docs/python/linting)). Try installing
   one for your editor!

2. Rewrite code challenges you've solved before or projects you've implemented
   before in a different language in Python. Start getting in as much practice
   with the language as possible!

3. Write a program to determine if a number, given on the command line, is prime.

   1. How can you optimize this program?
   2. Implement [The Sieve of
      Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
      of the oldest algorithms known (ca. 200 BC).

You must...
$ pip install .
...to make this file work.
"""
import sys
from math import sqrt, ceil
from time import time
from Stretch import is_prime as is_prime_cpp


def is_prime(num: int) -> bool:
    n = abs(num)
    if n == 1:
        return False
    for i in range(2, ceil(sqrt(n+1))):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':

    if len(sys.argv) == 2:
        d = sys.argv[1]
        print(d, 'is prime' if is_prime(int(d)) else 'is not prime')

    max_num = 1_000_000
    print('\nTime to count primes up to 1 million...\n')

    start = time()
    arr1 = [i for i in range(1, max_num) if is_prime(i)]
    print(f'Raw Python: {time() - start:.3f} sec.')

    start = time()
    arr2 = [i for i in range(1, max_num) if is_prime_cpp(i)]
    print(f'C-extension: {time() - start:.3f} sec.')
