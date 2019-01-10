"""
###############################
#print(AssertionError.mro())

try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")


###############################
#lst1 = ['ZeroDivisionError','OSError','ArithmeticError','FileNotFoundError']
#lst2 = []
#print(set(lst1) | set(lst2))

#in_lst = ['BaseException','Exception : BaseException, ErrorK','LookupError : Exception','KeyError : LookupError']
in_lst = ['1 : 2, 3, 4, 5, 6', '7 : 8, 3, 5', '8 : 3, 9', '2 : 7, 3, 5, 10, 9', '3 : 5, 9',
          '4 : 10', '5 : 9', '10', '6 : 4, 10', '9 : 6']
d = {}

for c in in_lst:
    #ln = input()
    ln = c.split(":")
    d[ln[0].strip(" ")] = [] if ln[0].strip(" ") not in d else d[ln[0].strip(" ")]
    if len(ln) == 2:
        for i in ln[1].split(","):
            i = i.strip(" ")
            d[ln[0].strip(" ")].extend([i])
            if i in d:
                d[ln[0].strip(" ")].extend(d[i])
            else:
                d[i] = []

for k, v in d.items(): print(k, "\t: ", *v)

#test_lst = ['BaseException','KeyError']
test_lst = ['5', '9', '1', '7', '8']
out_set = set()
while len(test_lst) > 0:
    l = test_lst.pop()
    if len(list(set(test_lst) & set(set(d[l])))) != 0:
        out_set.add(l)

print(*out_set)


###############################

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x < 0:
            raise NonPositiveError

        super(PositiveList, self).append(x)

lst = PositiveList()
lst.append(5)
lst.append(-5)


"""
###############################

#in_lst = ['BaseException','Exception : BaseException, ErrorK','LookupError : Exception','KeyError : LookupError']
in_lst = ['1 : 2, 3, 4, 5, 6', '7 : 8, 3, 5', '8 : 3, 9', '2 : 7, 3, 5, 10, 9', '3 : 5, 9',
          '4 : 10', '5 : 9', '10', '6 : 4, 10', '9 : 6']
d = {}

for c in in_lst:
    #ln = input()
    ln = c.split(":")
    d[ln[0].strip(" ")] = [] if ln[0].strip(" ") not in d else d[ln[0].strip(" ")]
    if len(ln) == 2:
        for i in ln[1].split(","):
            i = i.strip(" ")
            d[ln[0].strip(" ")].extend([i])
            if i in d:
                d[ln[0].strip(" ")].extend(d[i])
            else:
                d[i] = []

for k, v in d.items(): print(k, "\t: ", *v)

#test_lst = ['BaseException','KeyError']
test_lst = ['5', '9', '1', '7', '8']
out_set = set()
while len(test_lst) > 0:
    l = test_lst.pop()
    if len(list(set(test_lst) & set(set(d[l])))) != 0:
        out_set.add(l)

print(*out_set)
