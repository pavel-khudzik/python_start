"""

n1, n2 = (input() for _ in range(2))
op = input()
res = 0.0

if op in ("/", "mod", "div") and float(n2) == 0:
    res = "Деление на 0!"
else:
    if op == "+": res = (n1 + n2)
    elif op == "-": res = (n1 - n2)
    elif op == "/": res = (n1 / n2)
    elif op == "*": res = (n1 * n2)
    elif op == "mod": res = n1 % n2
    elif op == "pow": res = (n1 ** n2)
    elif op == "div": res = (n1 // n2)
print (res)

##################################################
shape = input()

if shape == "треугольник":
    a, b, c = (int(input()) for _ in range(3))
    p = (a+b+c)/2
    print ((p*(p-a)*(p-b)*(p-c)**0.5))
elif shape == "прямоугольник":
    a,b = (int(input()) for _ in range(2))
    print (a*b)
elif shape == "круг":
    r = int(input())
    print (3.14*(r**2))

##################################################
a, b, c, d = (int(input()) for _ in range(4))

for i in range(a-1, b+1):
    print("\t%d" % i if i != (a-1) else "\t", end="")
    for j in range(c, d+1):
        print("\t%d" % (i*j) if i != (a - 1) else "\t%d" % j, end="")
    print()

##################################################
a,b = int(input()), int(input())
a += -a%3
print(a)
b -= b%3
print(b)
print((a+b)/2)

##################################################
a, b = int(input()), int(input())
s = cnt = 0
if (a % 3) == 0:
    a = a
elif (a+1) % 3 == 0:
    a = a+1
else:
    a = a+2

for i in range(a, b+1, 3):
    s += i
    cnt +=1

print(s/cnt)

s = input()
print((s.upper().count("G")+s.upper().count("C"))/len(s)*100)

##################################################
s_in = 'aaaabbсaa' + ' '
s_out = ''
f_letter = s_in[0]
f_pos = 0

for i in range(len(s_in)):
    if s_in[i] != f_letter:
        s_out += s_in[f_pos] + str(i-f_pos)
        print(s_out, )
        f_letter = s_in[i]
        f_pos = i
        print(s_in[i:])

##################################################
#4 8 0 3 4 2 0 3
lst = sorted([int(i) for i in input().split()])
i = 0

while i < len(lst):
    if lst.count(lst[i]) > 1:
        print(lst[i], end=" ")
        i += lst.count(lst[i])
    else:
        i += 1

##################################################
n = 3
#1
a = [[0] * n] * n
print(*a)
a[0][0] = 5
print(*a)

#2
a = [[0] * n for _ in range(n)]
print(*a)
a[0][0] = 5
print(*a)

##################################################
lst = [int(input())]

while sum(lst) != 0:
    lst.append(int(input()))

print((i*i for i in lst))

##################################################
n, i = int(input()), 1
lst = ""

while n >= sum(range(i)):
    lst += ((str(i) + " ") * i)
    i += 1

print(*(lst.split()[:n]))

##################################################
lst = [int(i) for i in input().split()]
x = int(input())

if x not in lst:
    print("Отсутствует")
else:
    for i in range(len(lst)):
        if lst[i] == x:
            print(i, end=" ")


##################################################
# 9 5 3 | 0 7 -1 | -5 2 9
in_str = input()
mtrx = []
while in_str != 'end':
    mtrx.append([int(i) for i in in_str.split()])
    in_str = input()

for i, ln in enumerate(mtrx):
    new_ln = []
    for j in range(len(ln)):
        new_ln.append(mtrx[i][j-1] + mtrx[i][(j+1)-len(ln)] + mtrx[i-1][j] + mtrx[(i+1)-len(mtrx)][j])
    print(*new_ln)

###################################################
###################################################
def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return - x / 2
    else:
        return (x - 2) ** 2 + 1

print(f(4.5))
print(f(-4.5))
print(f(1))


###################################################
lst = [1, 2, 3, 4, 5, 6]

def modify_list(l):
    i = 0

    while i < len(l):
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
            i += 1
        else:
            l.remove(l[i])

print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]


###############################################
d = {}

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key * 2 in d:
        d[key * 2].append(value)
    else:
        d[key * 2] = [value]

print(d)
update_dictionary(d, 1, -1)
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}


#############################################
in_str = "a aa abC aa ac abc bcd a"
d = {}

for w in in_str.lower().split():
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

for k, v in d.items():
    print(k + ' ' + str(v))


##############################################
def f(x):
    return x * 10

#a=[int(input()) for i in range(int(input()))]
#b={x:f(x) for x in set(a)}
#print(*[b[x] for x in a], sep='\n')

n = int(input())
lst_x = [int(input()) for _ in range(n)]
d = {}

for x in lst_x:
    if x not in d:
        d[x] = f(x)

print(*[d[x] for x in lst_x], sep='\n')


out_lf = open("out_data.txt", "w")

with open("in_data.txt", "r") as in_fl:
    lines = in_fl.readlines()

for in_str in lines:
    in_str = in_str.strip()
    i = len(in_str)-1
    out_str = ""

    while i >= 0:
        if in_str[i] not in "0123456789":
            out_str = in_str[i:][0]*int(in_str[i:][1:]) + out_str
            in_str = in_str[:i]
        i -= 1

    out_lf.write(out_str + "\n")

out_lf.close()


##############################################
with open("in_data.txt", "r") as in_fl:
    lst = in_fl.read().strip().split()

#t = max(lst,key=lst.count)
#print(t , lst.count(t))

new_lst = [x.lower() for x in lst]
new_lst.sort()
el, cnt = "", 0

for i, v in enumerate(set(new_lst)):
    if i == 0:
        el = v
        cnt = new_lst.count(v)
    else:
        if new_lst.count(v) > cnt:
            el = v
            cnt = new_lst.count(v)
        elif new_lst.count(v) == cnt and v < el:
            el = v
            cnt = new_lst.count(v)

new_lst = [(x) for x in lst if x.lower() == el]
print (new_lst[0], cnt)

##############################################
with open("in_data.txt", "r", encoding="utf-8") as in_fl:
    lst = in_fl.read().split("\n")

lst = [x.split(";") for x in lst]

print(*(round((int(i[1])+int(i[2])+int(i[3]))/3, 9) for i in lst), sep="\n")
print(round(sum([int(i[1]) for i in lst])/len(lst), 9),
      round(sum([int(i[2]) for i in lst])/len(lst), 9),
      round(sum([int(i[3]) for i in lst])/len(lst), 9))

############################################################################
import requests

url = "https://stepic.org/media/attachments/course67/3.6.3/"

with open("in_data.txt", "r", encoding="utf-8") as in_fl:
    f_name = in_fl.readline()

while f_name != "":
    r = requests.get(f_name)
    print(f_name)
    if r.content.decode("utf-8").split()[0] == "We":
        open("out_data.txt", "w").write(r.content.decode("utf-8"))
        f_name = ""
    else:
        f_name = url + r.content.decode("utf-8")


##############################################
#Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#lst = ["Зенит;3;Спартак;1", "Спартак;1;ЦСКА;1", "ЦСКА;0;Зенит;2"]
lst = [input().split(";") for _ in range(int(input()))]
tab = {}

for l in lst:
    t1 = tab.setdefault(l[0], [0, 0, 0, 0, 0])
    t2 = tab.setdefault(l[2], [0, 0, 0, 0, 0])
    if l[1] > l[3]:
        t1[0] += 1
        t1[1] += 1
        t1[4] += 3

        t2[0] += 1
        t2[3] += 1
    elif l[1] < l[3]:
        t2[0] += 1
        t2[1] += 1
        t2[4] += 3

        t1[0] += 1
        t1[3] += 1
    else:
        t1[0] += 1
        t1[2] += 1
        t1[4] += 1

        t2[0] += 1
        t2[2] += 1
        t2[4] += 1

for k, v in tab.items():
    print("%s:%d %d %d %d %d" % (k, v[0], v[1], v[2], v[3], v[4]))


#####################################################
#abcd
#*d%#
#abacabadaba
##*%*d*%

ln1 = input()
ln2 = input()
ln_for_code = input()
ln_for_decode = input()

print(*[ln2[ln1.index(v)] for v in ln_for_code], sep="")
print(*[ln1[ln2.index(v)] for v in ln_for_decode], sep="")


#####################################################
dct = [input().lower() for _ in range(int(input()))]
text = [input().strip().split() for _ in range(int(input()))]
wrn = []

for ln in text:
    for l in ln:
        if l.lower() not in dct and l not in wrn:
            wrn += l

print(*wrn)


#####################################################
x = y = 0

dct = [input() for _ in range(int(input()))]

for l in dct:
    if l.split()[0] == "север":
        y += int(l.split()[1])
    elif l.split()[0] == "юг":
        y -= int(l.split()[1])
    elif l.split()[0] == "восток":
        x += int(l.split()[1])
    elif l.split()[0] == "запад":
        x -= int(l.split()[1])

print(x, y)


#####################################################
#c = {str(i):[0]*2 for i in range(1,12)}
#for l in open('in'):
#    s = l.strip().split()[::2]
#    c[s[0]] = [c[s[0]][0] + int(s[1]), c[s[0]][1] + 1]
#[print(k + ' ', v[0]/v[1] if v[0] else '-') for k, v in c.items()]

with open("in_data.txt", "r") as fl:
    text = fl.read().strip()

cl_lst = {k: [] for k in range(1, 12)}

for ln in text.split("\n"):
    inf = ln.strip().split("\t")
    cl_lst.get(int(inf[0])).append(int(inf[2]))

for k in cl_lst:
    if len(cl_lst[k]) == 0:
        print("%d -" % k)
    else:
        print("%d %f" % (k, sum(cl_lst[k]) / len(cl_lst[k])))


"""
#####################################################

l, i = 1, int(input())

x1, x2 = 0, i-1
y1, y2 = 0, i-1
mtx = [[0] * i for x in range(i)]

while l <= i**2:
    # A - > B
    for x in range(x1, x2+1):
        mtx[y1][x] = l
        l += 1

    # B -> C
    for y in range(y1+1, y2+1):
        mtx[y][x2] = l
        l += 1

    # C -> D
    for x in reversed(range(x1, x2)):
        mtx[y2][x] = l
        l += 1

    # D -> A
    for y in reversed(range(y1+1, y2)):
        mtx[y][x1] = l
        l += 1

    x1 += 1
    x2 -= 1
    y1 += 1
    y2 -= 1

for ln in mtx:
    print(*ln)

