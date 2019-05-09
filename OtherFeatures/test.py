import numpy as np
import matplotlib.pyplot as plt

x = np.arange(start=0,stop=2,step=0.4)


_list1 = [0.873589164785553, 0.9221218961625283, 0.9247554552294959, 0.8784800601956358, 0.8747178329571106]
_list2 = [0.8611738148984198, 0.9014296463506396, 0.9040632054176072, 0.8660647103085026, 0.8645598194130926]


# DL = [0.9131, 0.9145, 0.9120, 0.9132]
# labels = [u'Accuracy Rate', u'Precision', u'Recall', u'F-Measure']
plt.xticks((-0.1, 0.3, 0.7, 1.1, 1.5),(u'LR', u'RF', u'GBDT', u'NB', u'SVM'), fontsize = 14, family='Times New Roman')
plt.ylabel(u"Radio", fontsize = 14, family='Times New Roman')

total_width, n = 0.5, 5
width = total_width / n
x = x - (total_width - width) / 2

rects1=plt.bar(x, _list1, width=width, label='Decision Tree')
rects2=plt.bar(x + width, _list2, width=width, label='Logistic Regression')
# rects3=plt.bar(x + 2 * width, GDBT, width=width, label='DBSCAN')
# rects4=plt.bar(x + 3 * width, NB, width=width, label='Density Peaks')
#rects5=plt.bar(x + 4 * width, NB1, width=width, label='Canopy + Kmeans')
# plt.bar(x + 4 * width, DL, width=width, label='DL')
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        # 柱形图边缘用白色填充，纯粹为了美观
        rect.set_edgecolor('white')

# add_labels(rects1)
# add_labels(rects2)
# add_labels(rects3)
# add_labels(rects4)
#add_labels(rects5)

# box = plt.get_position()
# plt.set_position([box.x0, box.y0, box.width , box.height* 0.8])
plt.legend(loc='center left', bbox_to_anchor=(0.2, 1.05),ncol=5)
# plt.grid(axis= 'y',color='gray',linestyle='--',linewidth=1)
# plt.savefig("figure4bb.pdf")
plt.show()