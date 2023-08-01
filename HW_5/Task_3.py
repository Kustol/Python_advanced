'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
'''

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    fib_gen = fibonacci_generator()
    for __ in range(10):
        print(next(fib_gen))
