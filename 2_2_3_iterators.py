"""
################################

def gen():
    yield 1
    yield 2
    yield 3

for i in gen():
    print(i)


################################
import itertools

def primes():
    possiblePrime = 2
    while True:
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break

        if isPrime:
            yield possiblePrime

        possiblePrime += 1

print(list(itertools.takewhile(lambda x : x <= 31, primes())))

"""
################################
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return True if pos >= neg else False

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return True if pos >= 1 else False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return True if neg == 0 else False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.iterable:
            pos = neg = 0
            for fn in self.funcs:
                if len(list(filter(fn, [i]))) > 0:
                    pos += 1
                else:
                    neg += 1

            if self.judge(pos, neg):
                yield i


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
