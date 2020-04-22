
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

print("---------------------------------------NORMAL----------------------------------------------------------")
# NORMAL
def MNK(x,y):
    beta1 = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x*x) - np.mean(x) ** 2)
    beta0 = np.mean(y) - np.mean(x) * beta1
    return beta0, beta1

def rob(x,y):
    rQ = 0
    for i in range(len(x)):
        rQ += np.sign(x[i] - np.median(x)) * np.sign(y[i] - np.median(y))
    rQ /= len(x)

    l = int(len(y) / 4)
    if len(y) % 4 != 0:
        l += 1
    j = len(y) - l + 1

    beta1r = rQ * (y[j] - y[l]) / (x[j] - x[l])
    beta0r = np.median(y) - beta1r * np.median(x)

    return beta0r, beta1r


x = np.linspace(-1.8, 2, 20)
eps = norm.rvs(loc=0, scale=1, size=len(x))
y0 = 2 + 2 * x

y = 2 + 2 * x + eps

beta0, beta1 = MNK(x,y)
print('beta0 = ', beta0, 'beta1 =', beta1)
y1 = beta0 + beta1 * x

beta0r, beta1r = rob(x,y)
print('beta0r = ', beta0r, 'beta1r =', beta1r)
yr = beta0r + beta1r * x


plt.plot(x, y0, label='модель')
plt.plot(x, y1, label='МНК')
plt.plot(x, yr, label='МНМ')
plt.scatter(x, y, label='выборка')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


print("------------------------------------------------------------")



y[0] += 10
y[-1] -= 10

beta0, beta1 = MNK(x,y)
print('beta0 = ', beta0, 'beta1 =', beta1)
y1 = beta0 + beta1 * x

beta0r, beta1r = rob(x,y)
print('beta0r = ', beta0r, 'beta1r =', beta1r)
yr = beta0r + beta1r * x


plt.plot(x, y0, label='модель')
plt.plot(x, y1, label='МНК')
plt.plot(x, yr, label='МНМ')
plt.scatter(x, y, label='выборка')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
