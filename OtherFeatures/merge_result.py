import os

write_path = r'D:\data\weibo_dataset\topic.txt'
w_file = open(write_path, 'w')

dir_path = r'D:\data\weibo_dataset\coefficients'
files = os.listdir(dir_path)
for file in files:
    full_path = os.path.join(dir_path, file)
    with open(full_path, 'r') as f:
        line = f.readline().split()
        line = [int(ele) for ele in line]
        # print(line)
        line = [float(ele) / sum(line) for ele in line]
        # print(line)
        print(file[:-4], line)
#         w_file.write(file[:-4] + " " + str(line) + "\n")
# w_file.close()
