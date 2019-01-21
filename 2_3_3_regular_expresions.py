import re

#print(re.match.__doc__)
#print(re.search.__doc__)
#print(re.findall.__doc__)
#print(re.sub.__doc__)

# [] - можно указать множество подходящих символов
# . ^ $ * + ? { } [ ] \ | ( ) - метасимволы
# \d - [0-9]
# \D - [^0-9]
# \s - [ \t\n\r\f\v]
# \S - [^ \t\n\r\f\v]
# \w - [a-zA-Z0-9_]
# \W - [^a-zA-Z0-9_]

"""
pattern = r"abc"
string = "123abcdef"
match_object = re.match(pattern, string)
print("match -", match_object)
match_object = re.search(pattern, string)
print("search -", match_object)

### 2 ###
pattern = r"a[abc]c"
string = "acc"
match_object = re.match(pattern, string)
print("match -", match_object)
match_object = re.search(pattern, string)
print("search -", match_object)

string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)


### 3 ###
pattern = r"a[^a-d]c"
string = "azc"
match_object = re.match(pattern, string)
print("match -", match_object)
match_object = re.search(pattern, string)
print("search -", match_object)

pattern = r"a[\w.]c"
string = "abc, a.c, a-c, aBc, azc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r"a.c"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r"a[.]c"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
"""

### 4 ###