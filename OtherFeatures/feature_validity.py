import numpy as np
import logging
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    data_arrays = np.zeros((8858, 5))
    data_labels = np.zeros(8858)
    file_path = r'D:\data\weibo_dataset\normalize_features3.txt'
    # file_path = r'C:\Users\matebook\Desktop\normalize_features2.txt'
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]
    # for line in lines:
    #     print(line)
    #     print(line[1])
    for i in range(8858):
        data_arrays[i] = [float(ele) for ele in lines[i][:5]]
        # print(train_arrays[i])
        data_labels[i] = lines[i][5]
        # print(train_labels[i])
    print(data_arrays.shape, data_labels.shape)
    data_train, data_test, data_train_label, data_test_label = train_test_split(data_arrays, data_labels, test_size=0.3, random_state=0)
    print(data_train.shape, data_train_label.shape)
    print(data_test.shape, data_test_label.shape)

    res1 = []
    res2 = []
    # LR
    lr_clf = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True, intercept_scaling=1, random_state=None, tol=0.0001).fit(data_arrays, data_labels)
    test_labels_LR = lr_clf.predict(data_test.reshape(-1, 5))
    accuracy_score1 = accuracy_score(data_test_label, test_labels_LR)
    print(accuracy_score1)
    res1.append(accuracy_score1)

    # RF
    rf_clf = RandomForestClassifier(n_estimators=100).fit(data_train, data_train_label)
    test_labels_RF = rf_clf.predict(data_test.reshape(-1, 5))
    accuracy_score2 = accuracy_score(data_test_label, test_labels_RF)
    print(accuracy_score2)
    res1.append(accuracy_score2)

    # GBDT
    gbdt_clf = GradientBoostingClassifier(n_estimators = 100, max_depth = 4).fit(data_train, data_train_label)
    test_labels_GBDT = gbdt_clf.predict(data_test.reshape(-1, 5))
    accuracy_score3 = accuracy_score(data_test_label, test_labels_GBDT)
    print(accuracy_score3)
    res1.append(accuracy_score3)

    # NB
    nb_clf = GaussianNB().fit(data_train, data_train_label)
    test_labels_NB = nb_clf.predict(data_test.reshape(-1, 5))
    accuracy_score4 = accuracy_score(data_test_label, test_labels_NB)
    print(accuracy_score4)
    res1.append(accuracy_score4)

    # SVM
    svm_clf = svm.SVC(kernel='linear', C=1, probability=True).fit(data_train, data_train_label)
    test_labels_SVM = svm_clf.predict(data_test.reshape(-1, 5))
    accuracy_score5 = accuracy_score(data_test_label, test_labels_SVM)
    print(accuracy_score5)
    res1.append(accuracy_score5)

    data_arrays = np.zeros((8858, 4))
    data_labels = np.zeros(8858)
    # 去掉一个特征
    for i in range(8858):
        # 去掉F1
        data_arrays[i] = [float(ele) for ele in lines[i][1:5]]
        # 去掉F2
        # data_arrays[i] = [float(ele) for ele in lines[i][:1] + lines[i][2:5]]
        # 去掉F3
        # data_arrays[i] = [float(ele) for ele in lines[i][:2] + lines[i][3:5]]
        # 去掉F4
        # data_arrays[i] = [float(ele) for ele in lines[i][:3] + lines[i][4:5]]
        # 去掉F5
        # data_arrays[i] = [float(ele) for ele in lines[i][:4]]
        data_labels[i] = lines[i][5]
        # print(train_labels[i])
    print(data_arrays.shape, data_labels.shape)
    data_train, data_test, data_train_label, data_test_label = train_test_split(data_arrays, data_labels, test_size=0.3, random_state=0)
    print(data_train.shape, data_train_label.shape)
    print(data_test.shape, data_test_label.shape)

    # LR
    lr_clf = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True, intercept_scaling=1,
                                random_state=None, tol=0.0001).fit(data_arrays, data_labels)
    test_labels_LR = lr_clf.predict(data_test.reshape(-1, 4))
    accuracy_score1 = accuracy_score(data_test_label, test_labels_LR)
    print(accuracy_score1)
    res2.append(accuracy_score1)

    # RF
    rf_clf = RandomForestClassifier(n_estimators=100).fit(data_train, data_train_label)
    test_labels_RF = rf_clf.predict(data_test.reshape(-1, 4))
    accuracy_score2 = accuracy_score(data_test_label, test_labels_RF)
    print(accuracy_score2)
    res2.append(accuracy_score2)

    # GBDT
    gbdt_clf = GradientBoostingClassifier(n_estimators=100, max_depth=4).fit(data_train, data_train_label)
    test_labels_GBDT = gbdt_clf.predict(data_test.reshape(-1, 4))
    accuracy_score3 = accuracy_score(data_test_label, test_labels_GBDT)
    print(accuracy_score3)
    res2.append(accuracy_score3)

    # NB
    nb_clf = GaussianNB().fit(data_train, data_train_label)
    test_labels_NB = nb_clf.predict(data_test.reshape(-1, 4))
    accuracy_score4 = accuracy_score(data_test_label, test_labels_NB)
    print(accuracy_score4)
    res2.append(accuracy_score4)

    # SVM
    svm_clf = svm.SVC(kernel='linear', C=1, probability=True).fit(data_train, data_train_label)
    test_labels_SVM = svm_clf.predict(data_test.reshape(-1, 4))
    accuracy_score5 = accuracy_score(data_test_label, test_labels_SVM)
    print(accuracy_score5)
    res2.append(accuracy_score5)
    # histogram
    print(res1)
    print(res2)


    plt.xticks((-0.1, 0.3, 0.7, 1.1, 1.5), (u'LR', u'RF', u'GBDT', u'NB', u'SVM'), fontsize=14,
               family='Times New Roman')
    plt.ylabel(u"Radio", fontsize=14, family='Times New Roman')

    x = np.arange(start=0, stop=2, step=0.4)
    total_width, n = 0.5, 5
    width = total_width / n
    x = x - (total_width - width) / 2

    rects1 = plt.bar(x, res1, width=width, label='With F1')
    rects2 = plt.bar(x + width, res2, width=width, label='Without F1')

    plt.ylim(ymax=1)
    plt.ylim(ymin=0)

    plt.legend(loc='center left', bbox_to_anchor=(0.2, 1.02), ncol=5)
    # plt.grid(axis= 'y',color='gray',linestyle='--',linewidth=1)
    # plt.savefig("figure4bb.pdf")
    plt.show()
