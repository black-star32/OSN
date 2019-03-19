from math import exp
import matplotlib.pyplot as plt
import numpy as np
from numpy import cumsum

if __name__ == '__main__':
    dir_path = "D:/data/weibo_dataset/active_days.txt"
    with open(dir_path, 'r') as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]
        lines = [float(line[1]) for line in lines]
        print(lines)
        lines = sorted(lines)
        print(lines)
        X = lines
        Y = cumsum(X)
        Y = Y / sum(X)
        plt.plot(X,Y)
        plt.show()