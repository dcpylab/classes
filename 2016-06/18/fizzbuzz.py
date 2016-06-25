#
# FizzBuzz! Print the integers from 1 to 100, except for
# multiples of 3 print 'fizz', for multiples of 5 print 'buzz',
# and for multiples of both print 'fizzbuzz'
#
from __future__ import print_function


def is_multiple(factor, n):
    result = n % factor
    return (result == 0)


if __name__ == '__main__':
    integers = range(1, 101)
    for i in integers:
        if is_multiple(3, i) and is_multiple(5, i):
            print('FizzBuzz')
        elif is_multiple(3, i):
            print('Fizz')
        elif is_multiple(5, i):
            print('Buzz')
        else:
            print(i)
