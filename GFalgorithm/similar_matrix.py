import os
import re
import numpy as np

def readfile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

# dir_path1 = "D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/original_data/follows/"
# dir_path2 = "D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/original_data/follows/follows/"
# dir_path3 = "D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/similarly/"
dir_path1 = "D:/data/weibo_dataset/original_data/follows/"
dir_path2 = "D:/data/weibo_dataset/original_data/follows/follows/"
dir_path3 = "D:/data/weibo_dataset/similarly/"

file_list1 = os.listdir(dir_path1)
file_list2 = os.listdir(dir_path2)
pattern1 = re.compile(r'\d*.txt')
#读取dir_path1下所有txt文件
txt_file_list1 = pattern1.findall(str(file_list1))
#读取dir_path1下所有txt文件
txt_file_list2 = pattern1.findall(str(file_list2))
similary1 = []
similary2 = []
#遍历dir_path1目录下所有txt
for text_file1 in txt_file_list1:
    filename1 = os.path.join(dir_path1, text_file1)
    try:
        lines1 = readfile(filename1)
    except FileNotFoundError:
        continue
    effective_file_list = [line1 for line1 in lines1 if (line1[:-1] + ".txt") in txt_file_list2]
    for effective_file_1 in effective_file_list:
        filename2 = os.path.join(dir_path2, effective_file_1[:-1] + ".txt")
        lines2 = readfile(filename2)
        for effective_file_2 in effective_file_list:
            filename3 = os.path.join(dir_path2, effective_file_2[:-1] + ".txt")
            lines3 = readfile(filename3)
            intersection = list(set(lines2).intersection(set(lines3)))
            union = list(set(lines2).union(set(lines3)))
            #两个集合都为空
            if len(union) == 0:
                jaccard = 0
            else:
                jaccard = float(len(intersection)) / float(len(union))
            # print(jaccard)
            similary1.append(jaccard)
        similary2.append(similary1)
        similary1 = []
    print(np.array(similary2))
    result = np.array(similary2)
    filename4 = os.path.join(dir_path3, text_file1)
    # writefile(filename4, str(result))
    np.savetxt(filename4, result)
    # print(result.shape)
    similary2 = []
    # print(np.array(similary2))


    # for line1 in lines1:
    #     filename2 = line1[:-1] + ".txt"
    #     if filename2 in file_list2:
    #         full_filename2 = os.path.join(dir_path2, filename2)
    #         file2 = open(full_filename2, 'r')
    #         lines2 = file2.readlines()
    #         file2.close()
    #     for line2 in lines1:
    #         filename3 = line2[:-1] + ".txt"
    #         if filename3 in file_list2:
    #             full_filename3 = os.path.join(dir_path2, filename3)
    #             file3 = open(full_filename3, 'r')
    #             lines3 = file3.readlines()
    #             file3.close()
    #             intersection = list(set(lines2).intersection(set(lines3)))
    #             union = list(set(lines2).union(set(lines3)))
    #             #两个集合都为空的情况
    #             if len(union) == 0:
    #                 jaccard = 0
    #             else:
    #                 jaccard = float(len(intersection)) / float(len(union))
    #             similary1.append(jaccard)
    #         else:
    #             continue
    #     similary2.append(similary1)
    # file1.close()
    # print(np.array(similary2))
    # print(np.array(similary2).shape)


