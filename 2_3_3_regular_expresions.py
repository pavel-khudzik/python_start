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


### 4 ###
string = "aa, aba, abba, abbba, abbbba"
print(re.findall(r"ab?a", string))      # ['aa', 'aba']
print(re.findall(r"ab+a", string))      # ['aba', 'abba', 'abbba', 'abbbba']
print(re.findall(r"ab*a", string))      # ['aa', 'aba', 'abba', 'abbba', 'abbbba']
print(re.findall(r"ab{3}a", string))
print(re.findall(r"ab{2,4}a", string))


### 5 ###
pattern = r"(test|text)*"
string = "testtexttext"
match = re.match(pattern, string)
print(match)

pattern = r"((abc)|(test|text)*)"
match = re.match(pattern, "abc")
print(match)
print(match.groups())

match = re.match(pattern, "texttesttext")
print(match)
print(match.groups())

pattern = r"(\w+)-\1"
string = 'test-test chop-chop'
match = re.match(pattern, string)
print(match)
duplicates = re.sub(pattern, r"\1", string)
print(duplicates)

pattern = r"((\w+)-\2)"
string = 'test-test chop-chop'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)


### 6 ###
x = re.match(r"(te)*?xt", "TEXT", re.IGNORECASE | re.DEBUG)
print(x)

"""
import re

#lines = ["catcat", "catapult and cat"]
#for line in lines:
#    if re.search(r"\bcat\b", line):
#        print(line)


#lines = ["zabcz", "zzz", "zzxzz"]
#for line in lines:
#    if re.search(r"z\w{3}z", line):
#        print(line)

#lines = ["\w denotes word character", "No slashes here"]
#for line in lines:
#    if re.search(r"\\", line):
#        print(line)

#lines = ["this is a text", "this' !is. ?n1ce"]
#for line in lines:
#    print(re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line))

#lines = ["attraction", "buzzzz"]
#for line in lines:
#    print(re.sub(r"(\w)\1+", r"\1", line))


lines = ["blabla is a tandem repetition", "123123 is good too", "go go", "aaa"]
for line in lines:
    #print(line, re.findall(r"\b(\w+)(\1){1}\b", line))
    if re.search(r"\b(\w+)(\1){1}\b", line):
        print(line)
