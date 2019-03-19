'''

import random
from numpy import cumsum
import matplotlib.pyplot as plt
from scipy.stats import norm


def write_file(file_path, write_list):
    with open(file_path, 'w') as f:
        for line in write_list:
            f.write(str(line) + "\n")

if __name__ == '__main__':
    w_file_path1 = "D:/data/weibo_dataset/sample/negative_active_days.txt"
    w_file_path2 = "D:/data/weibo_dataset/sample/positive_active_days.txt"
    file_path = "D:/data/weibo_dataset/active_days.txt"
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]
        dic = {}
        print(lines)
        for line in lines:
            for index, item in enumerate(line[1:]):
                line[index+1] = float(item)
            dic[line[0]] = line[1]
        print(dic)
        active_days_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        print(active_days_dic)

    negative_sample = set()
    while len(negative_sample) < 107:
        sam = random.choice(active_days_dic[:400])
        negative_sample.add(sam)
    # print(negative_sample)
    negative_sample_list = list(negative_sample)
    positive_sample_list = []
    for line in active_days_dic:
        if line not in negative_sample_list:
            positive_sample_list.append(line)
    # print(negative_sample_list[0])
    # negative_sample_list = [line.split() for line in negative_sample_list]
    # print(negative_sample_list)
    negative_sample_list_value = [float(line[1]) for line in negative_sample_list]

    # positive_sample_list = [line.split() for line in positive_sample_list]

    positive_sample_list_value = [float(line[1]) for line in positive_sample_list]

    negative_lines = sorted(negative_sample_list_value)
    positive_lines = sorted(positive_sample_list_value)
    X1 = negative_lines
    print(X1)
    write_file(w_file_path1, X1)
    X2 = positive_lines
    print(X2)
    write_file(w_file_path2, X2)
    # Y1 = cumsum(X1)
    # Y2 = cumsum(X2)
    # Y1 = Y1 / sum(X1)
    # Y2 = Y2 / sum(X2)
    Y1 = norm.cdf(X1)
    print(Y1)
    Y2 = norm.cdf(X2)
    print(Y2)
    # plt.plot(X1, Y1)
    plt.plot(X2, Y2)
    plt.show()

'''

import matplotlib.pyplot as plt
from numpy import cumsum
from scipy.stats import norm


def read_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':
    file_path1 = "D:/data/weibo_dataset/sample/negative_active_days.txt"
    file_path2 = "D:/data/weibo_dataset/sample/positive_active_days.txt"
    negative_sample_list = read_file(file_path1)
    positive_sample_list = read_file(file_path2)

    negative_sample_list = [line.split() for line in negative_sample_list]
    negative_sample_list = [float(line[0]) for line in negative_sample_list]
    # print(negative_sample_list)
    positive_sample_list = [line.split() for line in positive_sample_list]
    positive_sample_list = [float(line[0]) for line in positive_sample_list]
    # print(positive_sample_list)
    X1 = negative_sample_list
    X2 = positive_sample_list
    # plt.hist(X1, normed=True, cumulative=True, histtype='step', bins=1000)
    # plt.hist(X2, normed=True, cumulative=True, histtype='step', bins=1000)
    # print(X2)
    # Y1 = norm.cdf(X1)
    # Y2 = norm.cdf(X2)
    # print(Y1)
    # print(Y2)
    Y1 = cumsum(X1)
    Y2 = cumsum(X2)
    Y1 = Y1 / sum(X1)
    Y2 = Y2 / sum(X2)
    plt.plot(X1, Y1, label='Positive sample')
    plt.plot(X2, Y2, label='Negative sample')

    plt.xlim(xmax=6)
    plt.xlim(xmin=0)
    plt.ylim(ymax=1)
    plt.ylim(ymin=0)
    plt.xlabel(u'avg_active_times', fontsize=12, family='Times New Roman')
    plt.ylabel(u'CDF', fontsize=12, family='Times New Roman')
    plt.legend(loc='lower right')
    # plt.legend()
    plt.savefig("D:/pycharm/PyCharm/projects/APT_OSN/figures/active_days_figure.pdf")
    plt.show()

    positive_sample_list = sorted(positive_sample_list)
    print(positive_sample_list)
    board = min(negative_sample_list)
    print(board)
    count = 0
    for sample in positive_sample_list:
        if sample < board:
            count+=1
    print(count)
    print(len(positive_sample_list))
    rate = count / len(positive_sample_list)
    print(rate)




