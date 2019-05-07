import random
import matplotlib.pyplot as plt
from numpy import cumsum
# i = random.choice((1, 2, 3))
def read_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines

def write_file(file_path, write_list):
    with open(file_path, 'w') as f:
        for line in write_list:
            f.write(line)

if __name__ == '__main__':
    file_path1 = r"D:\data\weibo_dataset\sample\negative_sample.txt"
    file_path2 = r"D:\data\weibo_dataset\sample\positive_sample.txt"
    negative_sample_list = read_file(file_path1)
    positive_sample_list = read_file(file_path2)
    # print(negative_sample_list[0])
    negative_sample_list = [line.split() for line in negative_sample_list]
    # print(negative_sample_list)
    negative_sample_list_value = [float(line[1]) for line in negative_sample_list]

    positive_sample_list = [line.split() for line in positive_sample_list]

    positive_sample_list_value = [float(line[1]) for line in positive_sample_list]

    negative_lines = sorted(negative_sample_list_value)
    positive_lines = sorted(positive_sample_list_value)

    X1 = negative_lines
    print(X1)
    X2 = positive_lines
    print(X2)
    threshold = 1.26
    negative_num = 0
    positive_num = 0
    TPR = []
    FPR = []
    while threshold < 2.19:
        for x1 in X1:
            if x1 < threshold:
                negative_num += 1
        for x2 in X2:
            if x2 < threshold:
                positive_num += 1
        #
        tpr = negative_num / len(X1)
        fpr = positive_num / len(X2)
        negative_num = 0
        positive_num = 0
        print(threshold)
        print(tpr)
        print(fpr)
        TPR.append(tpr)
        FPR.append(fpr)
        threshold += 0.01
    # Y1 = cumsum(X1)
    # Y2 = cumsum(X2)
    # Y1 = Y1 / sum(X1)
    # Y2 = Y2 / sum(X2)
    # plt.plot(X1, Y1, label='Negative sample')
    # plt.plot(X2, Y2, label='Positive sample')
    S = 0
    for i in range(len(TPR)-1):
        S = S + (FPR[i+1] - FPR[i]) * TPR[i]
    print(S)
    dis = 100
    change = 100
    for i in range(len(TPR)):
        if TPR[i]!=1 and FPR[i]!=0:
            dis = min(dis, pow(FPR[i],2)+pow(1-TPR[i],2))
            if dis!=change:
                print(FPR[i],TPR[i])
            change = dis
    print(dis)
    plt.xlim(xmax=1)
    plt.xlim(xmin=0)
    plt.ylim(ymax=1.01)
    plt.ylim(ymin=0)
    plt.xlabel(u'False Positive Rate', fontsize=12, family='Times New Roman')
    plt.ylabel(u'True Positive Rate', fontsize=12, family='Times New Roman')
    plt.grid()
    plt.plot(FPR, TPR)
    plt.savefig(r"D:\pycharm\PyCharm 2018.3.2\projects\OSN\figures\roc_figure.pdf")

    plt.show()