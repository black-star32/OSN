import numpy as np
import matplotlib.pyplot as plt
import math
# a = [24, 9, 8, 7, 6, 6, 6, 5, 4, 3, 2, 2, 2, 2, 1, 1, 1, 1]
# a = np.array(a)
# print(np.var(a))
# print(np.std(a))
# b = [13, 9, 7, 6, 5, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1]
# b = np.array(b)
# print(np.var(b))
# print(np.std(b))
Y = [24, 9, 8, 7, 6, 6, 6, 5, 4, 3, 2, 2, 2, 2, 1, 1, 1, 1]
# Y = [5, 4, 3, 3, 2, 2, 1, 1, 1]
X = []
XX = []
YY = []
for i in range(len(Y)):
    X.append(i)
    print(X[i],Y[i])
    if i != 0:
        print(0-X[i], Y[i])
Y = [y / sum(Y) for y in Y]
# plt.bar(range(len(Y)), Y)
XX.extend(X)
plt.plot(X,Y,'b')
# plt.bar(X, Y)
X = [-x for x in X]
XX.extend(X)
# plt.bar(X, Y)
plt.plot(X,Y,'b')
# y=1/(sqrt(2*pi)*a)*exp(-((x^2)/(2*(a^2))))
sig = 0.0166225950173507
# sig = 0.0797884560832824
u = 0
x = np.linspace(u - 3 * sig, u + 3* sig, 100)
y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
YY.append(y_sig)
print(XX)
print(YY)
print(len(XX))
print(len(YY))
YY = [y / sum(Y) for y in YY]
plt.plot(x,y_sig/90,'r')
plt.xlabel(u'topic', fontsize=12, family='Times New Roman')
plt.ylabel(u'the proportion of topic', fontsize=12, family='Times New Roman')

# plt.xlim(xmax=0.5)
# plt.xlim(xmin=-0.5)
plt.xlim(xmax=8)
plt.xlim(xmin=-8)
# plt.savefig("D:/pycharm/PyCharm/projects/APT_OSN/figures/topic_figure9.pdf")
plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# import math
#
# u = 0  # 均值μ
# u01 = -2
# sig = 0.0166225950173507 # 标准差δ
#
# x = np.linspace(u - 3 * sig, u + 3 * sig, 50)
# y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
# # y=1/(sqrt(2*pi)*a)*exp(-((x^2)/(2*(a^2))))
#
# print(x)
# print("=" * 20)
#
# print(y_sig)
#
# plt.plot(x, y_sig, "r-", linewidth=2)
# plt.grid(True)
# plt.show()