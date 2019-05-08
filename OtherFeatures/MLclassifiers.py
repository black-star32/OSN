import numpy as np
import logging
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc


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

    # LR
    lr_clf = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True, intercept_scaling=1, random_state=None, tol=0.0001).fit(data_arrays, data_labels)

    # RF
    rf_clf = RandomForestClassifier(n_estimators=100).fit(data_train, data_train_label)

    # GBDT
    gbdt_clf = GradientBoostingClassifier(n_estimators = 100, max_depth = 4).fit(data_train, data_train_label)

    # NB
    nb_clf = GaussianNB().fit(data_train, data_train_label)

    # SVM
    svm_clf = svm.SVC(kernel='linear', C=1, probability=True).fit(data_train, data_train_label)

    # 对Test数据进行预测
    test_labels_LR = []
    test_labels_RF = []
    test_labels_GBDT = []
    test_labels_NB = []
    test_labels_SVM = []
    temp_LR = []
    temp_RF = []
    temp_GBDT = []
    temp_NB = []
    temp_SVM = []
    # fm = open("mr.txt","w")
    # print(test_arrays[1])
    # res = classifier.predict_proba(test_arrays[1].reshape(-1, 100))
    # print(res)
    for i in range(len(data_test)):
        try:
            print(i)
            temp_LR = lr_clf.predict_proba(data_test[i].reshape(-1, 5))
            test_labels_LR.append(temp_LR[0][0])
            temp_SVM = svm_clf.predict_proba(data_test[i].reshape(-1, 5))
            test_labels_SVM.append(temp_SVM[0][0])
            # print(temp_SVM)
            # print(temp_SVM[0])
            # print(temp_SVM[0][0])

            # print(classifier.predict(test_arrays[i]))
            # fm.write(str(classifier.predict(test_arrays[i]))+"\n")
            temp_RF = rf_clf.predict_proba(data_test[i].reshape(-1, 5))
            test_labels_RF.append(temp_RF[0][0])
            temp_GBDT = gbdt_clf.predict_proba(data_test[i].reshape(-1, 5))
            test_labels_GBDT.append(temp_GBDT[0][0])
            temp_NB = nb_clf.predict_proba(data_test[i].reshape(-1, 5))
            test_labels_NB.append(temp_NB[0][0])


        except DeprecationWarning:
            continue

    log.info("预测完毕")

    fpr1, tpr1, thresholds1 = roc_curve(data_test_label, test_labels_LR, pos_label=0)
    auc1 = auc(fpr1, tpr1)
    print("LR:{}".format(auc1))
    plt.plot(fpr1, tpr1, 'b', label='LR')

    fpr2, tpr2, thresholds2 = roc_curve(data_test_label, test_labels_RF, pos_label=0)
    auc2 = auc(fpr2, tpr2)
    print("RF:{}".format(auc2))
    plt.plot(fpr2, tpr2, 'g', label='RF')

    fpr3, tpr3, thresholds3 = roc_curve(data_test_label, test_labels_GBDT, pos_label=0)
    auc3 = auc(fpr3, tpr3)
    print("GBDT:{}".format(auc3))
    plt.plot(fpr3, tpr3, 'r', label='GBDT')

    fpr4, tpr4, thresholds4 = roc_curve(data_test_label, test_labels_NB, pos_label=0)
    # print(fpr4)
    auc4 = auc(fpr4, tpr4)
    print("NB:{}".format(auc4))
    plt.plot(fpr4, tpr4, 'y', label='NB')

    fpr5, tpr5, thresholds5 = roc_curve(data_test_label, test_labels_SVM, pos_label=0)
    # print(fpr5)
    auc5 = auc(fpr5, tpr5)
    print("SVM:{}".format(auc5))
    plt.plot(fpr4, tpr4, 'fuchsia', label='SVM')
    # print(data_test_label)
    # print(test_labels_NB)
    # print(fpr4)
    # print(tpr4)

    plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='FPR = TPR')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])

    plt.xlabel('False Positive Rate', fontsize=14)
    plt.ylabel('True Positive Rate', fontsize=14)
    # plt.title('ROC curve')
    plt.legend(loc="lower right")
    plt.grid(True)
    # plt.savefig("figure5.pdf")
    plt.show()
