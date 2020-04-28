
import numpy as np
from scipy.stats import norm, chi2, t


# NORMAL
def m1(x, alpha):
    n = x.size
    s = np.var(x)
    x_ = np.mean(x)
    t_ = t.ppf(1 - alpha/2, n - 1)
    num = s * t_ / np.sqrt(n - 1)
    ml = x_ - num
    mr = x_ + num
    return ml, mr

def m2(x, alpha):
    n = x.size
    s = np.var(x)
    x_ = np.mean(x)
    u_ = norm.ppf(1 - alpha / 2)
    num = s * u_ / np.sqrt(n)
    ml = x_ - num
    mr = x_ + num
    return ml, mr

def s1(x, alpha):
    n = x.size
    s = np.var(x)
    hl = chi2.ppf(1 - alpha/2, n - 1)
    hr = chi2.ppf(alpha/2, n - 1)
    sl = s * np.sqrt(n) / np.sqrt(hl)
    sr = s * np.sqrt(n) / np.sqrt(hr)
    return sl, sr

def s2(x, alpha):
    n = x.size
    s = np.var(x)
    u = norm.ppf(1 - alpha/2)
    sl = s / np.sqrt(1 + u * np.sqrt((np.e + 2) / n))
    sr = s / np.sqrt(1 - u * np.sqrt((np.e + 2) / n))
    return sl, sr



size = [20, 100]

for i in range(len(size)):
    print('size = ', size[i])
    alpha = 0.05
    x = norm.rvs(loc=0, scale=1, size=size[i])
    ml, mr = m1(x, alpha)
    print(ml, mr)

    sl, sr = s1(x, alpha)
    print(sl, sr)

    ml, mr = m2(x, alpha)
    print(ml, mr)

    sl, sr = s2(x, alpha)
    print(sl, sr)
