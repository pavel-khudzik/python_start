"""

###############################
fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31))

###############################
print(sum([int(input()) for i in range(int(input()))]))

###############################
x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
print("s = %d" % id(s))
print("t = %d" % id(t))
t = t + "4"
print("t = %d" % id(t))

print(str(x) + " " + s)

###############################
objects = [1, 2, 1, 2, 3]

lst = []
for obj in objects:
    lst.append(id(obj))

print(len(set(lst)))

###############################
def closest_mod_5(x):
    while x % 5 != 0:
        x += 1

    return x

print(closest_mod_5(11))

###############################

n, k = map(int, input().split())

def C(n, k):
    if k == 0:
        return 1

    if k > n:
        return 0

    return C(n - 1, k) + C(n - 1, k - 1)

print(C(n,k))


###############################
d = {"global": ["", []]}

def get_nm(nmsp, var):
    if var in d[nmsp][1]:
        return nmsp
    elif d[nmsp][0] == "":
        return "None"
    else:
        return get_nm(d[nmsp][0], var)


#d["global"][0] = "par"
#d["global"][1].append(1)
#print(d)

with open("namespace.txt") as fl:
    for i in range(9):
        ln = fl.readline().strip()

        #print(ln.split())
        cmd, nmsp, var = ln.split()

        if cmd == "add":
            #print("add")
            d[nmsp][1].append(var)
        elif cmd == "create":
            #print("create")
            d[nmsp] = [var, []]
        else: #get
            print(get_nm(nmsp, var))



###############################
class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.coin_cnt = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.coin_cnt + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        self.coin_cnt += v


###############################
class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.lst = []

    def add(self, *a):
        # добавить следующую часть последовательности
        self.lst += a

        while len(self.lst) >= 5:
            print(sum(self.lst[0:5]))
            self.lst[:] = self.lst[5:]

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке,
        # в котором они были добавлены
        return self.lst


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]

###############################
d = {}

def is_parent(prnt, chld):
    res = list()
    if prnt == chld or prnt in d[chld]:
        return "Yes"
    elif len(d[chld]) == 0:
        return "No"
    else:
        for ch in d[chld]:
            res.append(is_parent(prnt, ch))
        if "Yes" in res:
            return "Yes"
        else:
            return "No"

#for _ in range(int(input())):
#    ln = input()
for ln in ["A : C B", "B : D E"]:
    d[ln.split(":")[0].strip(" ")] = []
    if len(ln.split(":")) == 2:
        for el in ln.split(":")[1].split():
            d[ln.split(":")[0].strip(" ")].append(el)
            if el not in d:
                d[el] = []


for ln in ['E A']:
    if len(ln.split()) == 2:
        print(is_parent(ln.split()[0], ln.split()[1]))
    else:
        print(is_parent(ln.split()[0], ln.split()[0]))

#BEST
#n = int(input())
#parents = {}
#for _ in range(n):
#    a = input().split()
#    parents[a[0]] = [] if len(a) == 1 else a[2:]

#def is_parent(child, parent):
#    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))

#q = int(input())
#for _ in range(q):
#    a, b = input().split()
#    print("Yes" if is_parent(b, a) else "No")


###############################
class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())

###############################
import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, T):
        super(LoggableList, self).append(T)
        self.log(T)

x = LoggableList([1, 2])
x.append(3)

"""
###############################

