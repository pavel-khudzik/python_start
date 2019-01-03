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


"""
###############################


