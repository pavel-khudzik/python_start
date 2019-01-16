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