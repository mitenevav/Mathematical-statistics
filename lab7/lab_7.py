
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, chi2, uniform

print("---------------------------------------NORMAL----------------------------------------------------------")
# NORMAL
def MLE(x):
    mu = np.mean(x)
    sigma = np.std(x)
    return mu, sigma

def hiN(x, k, step, a0):
    size = x.size
    n = []
    p = []
    a = []
    np = []
    nnp = []
    hi = []

    ni = x[x <= a0].size
    pi = norm.cdf(a0)
    npi = size * pi
    nnpi = ni - npi
    hii = nnpi ** 2 /npi

    n.append(ni)
    p.append(pi)
    np.append(npi)
    nnp.append(nnpi)
    hi.append(hii)

    for i in range(k-2):
        a1 = a0 + step
        ni = x[(x > a0) & (x <= a1)].size
        pi = norm.cdf(a1) - norm.cdf(a0)
        npi = size * pi
        nnpi = ni - npi
        hii = nnpi ** 2 / npi

        n.append(ni)
        p.append(pi)
        np.append(npi)
        nnp.append(nnpi)
        hi.append(hii)
        a.append(a0)

        a0 += step

    ni = x[x > a0].size
    pi = 1 - norm.cdf(a0)
    npi = size * pi
    nnpi = ni - npi
    hii = nnpi ** 2 / npi

    n.append(ni)
    p.append(pi)
    np.append(npi)
    nnp.append(nnpi)
    hi.append(hii)
    a.append(a0)

    return a, n, p, np, nnp, hi

size = 100
k = 7
alpha = 0.05
step = 0.45
a0 = -1

x = norm.rvs(loc=0, scale=1, size=size)
x.sort()
h = chi2.ppf(1 - alpha, k - 1)

mu, sigma = MLE(x)
a, n, p, np, nnp, hii = hiN(x, k, step, a0)

print('mu = ', mu, 'sigma = ', sigma)
print(a)
print(n)
print(p)
print(np)
print(nnp)
print(hii)
print(sum(n))
print(sum(p))
print(sum(np))
print(sum(nnp))
print(sum(hii))
print('hi = ', h)

print("---------------------------------------------------------------------------------------")
a0 = -1.5
loc = -2
sc = 4
step = 0.85
k = 5
h = chi2.ppf(1 - alpha, k - 1)

num = 0
for i in range(10000):
    y=uniform.rvs(loc=loc, scale=sc, size=20)
    a, n, p, np, nnp, hii = hiN(y, k, step, a0)
    if sum(hii) < h:
        num += 1


print(a)
print(n)
print(p)
print(np)
print(nnp)
print(hii)
print(sum(n))
print(sum(p))
print(sum(np))
print(sum(nnp))
print(sum(hii))
print('hi = ', h)
print(num)
