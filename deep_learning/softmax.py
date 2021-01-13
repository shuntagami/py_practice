import numpy as np
import matplotlib.pylab as plt

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

x = np.arange(-5, 5, 0.1)
y = softmax(x)
print(y)
print(np.sum(y))
# plt.plot(x, y)
# plt.show()
