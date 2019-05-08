import os
from sklearn import preprocessing
import numpy as np

if __name__ == '__main__':
    '''
    normalize_features3.txt
    re_follow
    active_days_figure
    similarly
    interaction
    D:\data\weibo_dataset\coefficients
    
    '''
    dir_path = r'D:\data\weibo_dataset'
    active_days_file =  os.path.join(dir_path, 'active_days.txt')
    interaction_file = os.path.join(dir_path, 'interaction.txt')
    re_follow_file = os.path.join(dir_path, 're_follow.txt')
    similary_file = os.path.join(dir_path, 'similarly.txt')
    topic_file = os.path.join(dir_path, 'symoy.txt')
    f1 = open(active_days_file, 'r')
    f2 = open(re_follow_file, 'r')
    f3 = open(interaction_file, 'r')
    f4 = open(similary_file, 'r')
    f5 = open(topic_file, 'r')
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    lines3 = f3.readlines()
    lines4 = f4.readlines()
    lines5 = f5.readlines()

    _dict = {}
    for line in lines1:
        line = line.split()
        # print(line)
        _dict[line[0]] = [line[1]]
        # print(_dict)

    for line in lines2:
        line = line.split()
        if line[0] not in _dict:
            continue
        _dict[line[0]].append(line[1])

    for line in lines3:
        line = line.split()
        if line[0] not in _dict:
            continue
        _dict[line[0]].append(line[1])

    for line in lines4:
        line = line.split()
        if line[0] not in _dict:
            continue
        _dict[line[0]].append(line[1])

    for line in lines5:
        line = line.split()
        if line[0] not in _dict:
            continue
        _dict[line[0]].append(line[2][:-1])



    _dict2 = {}
    for k, v in _dict.items():
        if len(_dict[k]) < 5:
            continue
        _dict2[k] = v

    i = 0
    X = np.zeros((len(_dict2), 5))
    for k, v in _dict2.items():
        X[i] = v
        i += 1
    print(X)
    # 标准化
    X_scaled = preprocessing.scale(X)
    print(X_scaled)





