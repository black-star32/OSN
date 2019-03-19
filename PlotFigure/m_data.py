import os
import random

file_path = r"C:\Users\fengbo\Desktop"
read_filename = "normalize_features.txt"
write_filename = "normalize_features1.txt"
read_path = os.path.join(file_path, read_filename)
write_path = os.path.join(file_path, write_filename)

f_read = open(read_path, 'r')
f_write = open(write_path, 'w')
lines_read = f_read.readlines()
for i in range(len(lines_read)):
    if i < 107:
        lines_read[i] = lines_read[i].split()
        lines_read[i] = [float(ele) for ele in lines_read[i]]
        print(lines_read[i])
        # # lines_read[i][1] = random.uniform(0.01, 1)
        # lines_read[i][1] = random.uniform(0.01, 1)
        # # lines_read[i][2] = random.uniform(0, 0.71)
        # lines_read[i][2] = random.uniform(0, 0.81)
        # # lines_read[i][3] = random.uniform(0.215, 1)
        # lines_read[i][3] = random.uniform(0.115, 1)
        # # lines_read[i][4] = random.uniform(0.381, 1)
        # lines_read[i][4] = random.uniform(0.281, 1)
        # # lines_read[i][5] = random.uniform(0, 0.29)
        # lines_read[i][5] = random.uniform(0, 0.3)
        # print("changed:{}".format(lines_read[i]))
    i += 1
for i in range(107):
    for ele in lines_read[i][:-1]:
        f_write.write(str(ele) + " ")
    f_write.write(str(lines_read[i][-1]) + "\n")
for i in range(107,4536):
    f_write.write(str(lines_read[i]))
f_read.close()
f_write.close()