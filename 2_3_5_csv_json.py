"""
import csv

primary_type_pos = 0
first_row = True
crimes_dict = {}

with open("crimes.csv", "r") as f:
    csv_rows = csv.reader(f)

    for row in csv_rows:
        if first_row:
            #print(row)
            primary_type_pos = row.index("Primary Type")
            #print(primary_type_pos)
            first_row = False
        else:
            #print(row)
            #print(row[primary_type_pos])
            crimes_dict[row[primary_type_pos]] = crimes_dict.setdefault(row[primary_type_pos], 0) + 1

crimes_dict = sorted(crimes_dict.items(), key=lambda kv: kv[1], reverse=True)

print(crimes_dict, sep="\n")

"""

