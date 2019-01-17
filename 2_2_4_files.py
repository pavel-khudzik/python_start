"""
lst = []

with open("in_data.txt", "r") as inf:
    for l in inf:
        lst.append(l.strip())

print(lst)

with open("out_data.txt", "w") as outf:
    outf.write("\n".join(reversed(lst)))

### 1
with open('dataset_24465_4.txt', 'r') as fr, open('dataset_24465_4_w.txt', 'w') as fw:
    fw.writelines(fr.readlines()[::-1])

### 2
lines = open("input.txt").readlines()
with open("output.txt", "w") as out:
    out.writelines(reversed(lines))

##########################################
import os

print(os.getcwd())
print(*(os.listdir()), sep="\n")

# os.chdir(r"d:\\")

for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)

"""
##########################################
import os

os.chdir(r"d:\\- python")
for current_dir, dirs, files in os.walk("."):
    #print(current_dir, dirs, files)
    if list(filter(lambda x: x.endswith('.py'), files)):
        print(current_dir[2:].replace("\\", "/"))

"""
import os

result = [cur_dir for cur_dir, dirs, files in os.walk("main") if any((fl.endswith(".py")
    for fl in files))]

with open("py_dirs.txt", "w") as w:
    w.write("\n".join(sorted(result)))
"""
