import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import os
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram


if __name__ == '__main__':
    dir_path = r'D:\data\weibo_dataset\similarly'
    write_path = r'D:\data\weibo_dataset\similarly2.txt'
    w_file = open(write_path, 'w')
    file_list = os.listdir(dir_path)
    for file in file_list:
        full_path = os.path.join(dir_path, file)
        with open(full_path, 'r') as f:
            lines = f.readlines()
            list2 = []
            for line in lines:
                list1 = []
                for num in line.split():
                    list1.append(float(num))
                    # list1.append(num)
                list2.append(list1)
        mat = np.matrix(list2)
        print(mat)
        variables = [i for i in range(len(mat))]
        print(variables)
        labels = variables
        # 层次聚类树
        try:
            df = pd.DataFrame(mat, columns=variables, index=labels)
        except AssertionError:
            continue
        print(df)

        # 计算距离关联矩阵，两两样本间的欧式距离
        # row_dist = pd.DataFrame(squareform(pdist(df,metric='euclidean')),columns=labels,index=labels)
        # print (row_dist)
        # print (help(linkage))
        row_clusters = linkage(pdist(df, metric='euclidean'), method='complete')  # 使用抽秘籍距离矩阵
        # row_clusters = linkage(df.values,method='complete',metric='euclidean')
        print(pd.DataFrame(row_clusters, columns=['row label1', 'row label2', 'distance', 'no. of items in clust.'],
                           index=['cluster %d' % (i + 1) for i in range(row_clusters.shape[0])]))
        # print(row_clusters)
        i = 0
        for i in range(len(row_clusters)):
            print(row_clusters[i][2])
            if row_clusters[i][2] >= math.sqrt(2):
                break
        clusters = len(mat) - i
        print(clusters)

        # # 层次聚类树
        # row_dendr = dendrogram(row_clusters, labels=labels)
        # plt.tight_layout()
        # plt.ylabel('Euclidean distance')
        # filename = file[:-4] + '.pdf'
        # save_path = os.path.join(r'D:\data\weibo_dataset\clusterfigure', filename)
        # plt.savefig(save_path)
        # # plt.show()
        # plt.clf()
        w_file.write(file[:-4] + " " + str(clusters) + "\n")
    w_file.close()