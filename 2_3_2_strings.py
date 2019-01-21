"""
##########################################
s = input()
a = input()
b = input()

i = 0

while (i <=1000) and (a in s):
    s = s.replace(a, b)
    i += 1

print(i if i <= 1000 else "Impossible")

"""
##########################################

s = "abababa"
t = "aba"

pos = s.find(t)
cnt = 0

while pos >=0:
    cnt += 1
    pos = s.find(t, pos+1)

print(cnt)