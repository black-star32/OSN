# import numpy as np
# import matplotlib.pyplot as plt
#
# filename = 'D:/data/weibo_dataset/sample/positive_sample.txt'
#
# def read_file(file_path):
#     with open(file_path, 'r') as f:
#         lines = f.readlines()
#     return lines
#
# if __name__ == '__main__':
#     positive_sample_list = read_file(filename)
#     positive_sample_list = [line.split() for line in positive_sample_list]
#     positive_sample_list = [float(line[0]) for line in positive_sample_list]
#     dataSets = []
#
#     for line in positive_sample_list:
#     #print(line)
#         try:
#             dataSets.append(line)
#         except :
#             print("Error: Exception Happened... \nPlease Check Your Data Format... ")
#
#     temp = []
#     for set in dataSets:
#         temp2 = []
#         for item in set:
#             if item!='':
#                 temp2.append(float(item))
#         temp2.sort()
#         temp.append(temp2)
#     dataSets = temp
#
#     for set in dataSets:
#
#         plotDataset = [[],[]]
#         count = len(set)
#         for i in range(count):
#
#             plotDataset[0].append(float(set[i]))
#             plotDataset[1].append((i+1)/count)
#         print(plotDataset)
#         plt.plot(plotDataset[0], plotDataset[1], '-', linewidth=2)
#
#     plt.show()

# L = [24,9,8,7,6,6,6,5,4,3,2,2,2,2,1,1,1,1]
L = [5,4,3,3,2,2,1,1,1]
for l in L:
    print("%.2f"%(l/sum(L)),end=",")
