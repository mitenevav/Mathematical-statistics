import seaborn as sns
from pylab import *
from scipy.stats import *
from numpy import random
from matplotlib import*
import matplotlib.pyplot as plt


buf_size = [20, 60, 100]

print("---------------------------------------NORMAL----------------------------------------------------------")
# NORMAL
fig, ax = plt.subplots(1, 3)
for i in range(len(buf_size)):
    x = linspace(-4,4,1000)
    y = norm.cdf(x)
    plt.subplot(1, len(buf_size), i + 1)
    plt.plot(x,y)

    y=linspace(0,1,buf_size[i])
    y.sort()
    x = norm.rvs(scale=1, size=buf_size[i])
    x.sort()

    for j in range(buf_size[i]):
        if x[j] < -4:
            x[j] = -4
        elif x[j]>4:
            x[j] = 4

    yy = empty(buf_size[i]*2)
    yy[0] = 0
    yy[1] = y[0]
    for j in range(buf_size[i]-1):
        yy[j*2 + 2] = y[j+1]
        yy[j * 2 + 3] = y[j+1]

    xx = empty(buf_size[i] * 2)
    xx[0] = -4
    for j in range(buf_size[i]-1):
        xx[j*2 + 1] = x[j]
        xx[j * 2 + 2] = x[j]
    xx[buf_size[i] * 2 - 1] = 4


    plt.plot(xx, yy)
    plt.title('Normal, n='+ str(buf_size[i]))

plt.show()

for i in range(len(buf_size)):
    fig, ax = plt.subplots(1, 3)

    x = linspace(-4,4,1000)

    y = norm.pdf(x, 0, 1)
    ax[0].plot(x,y)
    ax[1].plot(x, y)
    ax[2].plot(x, y)

    x = norm.rvs(scale=1, size=buf_size[i])
    x = x[x <= 4]
    x = x[x >= -4]
    x.sort()


    kde = gaussian_kde(x)
    kde.set_bandwidth(bw_method='silverman')
    h_n = kde.factor

    sns.kdeplot(x, ax=ax[0], bw=h_n/2)
    sns.kdeplot(x, ax=ax[1], bw=h_n)
    sns.kdeplot(x, ax=ax[2], bw=h_n*2)

    ax[0].set_title(r'$h = \frac{h_n}{2}$')
    ax[1].set_title(r'$h = h_n$')
    ax[2].set_title(r'$h = h_n*2$')

    plt.suptitle('Normal, n='+ str(buf_size[i]))
    plt.show()


print()
print("---------------------------------------LAPLACE----------------------------------------------------------")
#   LAPLACE
for i in range(len(buf_size)):
    x = linspace(-4, 4, 1000)
    y = laplace.cdf(x)
    plt.subplot(1, len(buf_size), i + 1)
    plt.plot(x, y)

    y = linspace(0, 1, buf_size[i])
    y.sort()
    x = laplace.rvs(scale = sqrt(1/2),size=buf_size[i])
    x.sort()

    for j in range(buf_size[i]):
        if x[j] < -4:
            x[j] = -4
        elif x[j] > 4:
            x[j] = 4

    yy = empty(buf_size[i] * 2)
    yy[0] = 0
    yy[1] = y[0]
    for j in range(buf_size[i] - 1):
        yy[j * 2 + 2] = y[j + 1]
        yy[j * 2 + 3] = y[j + 1]

    xx = empty(buf_size[i] * 2)
    xx[0] = -4
    for j in range(buf_size[i] - 1):
        xx[j * 2 + 1] = x[j]
        xx[j * 2 + 2] = x[j]
    xx[buf_size[i] * 2 - 1] = 4

    plt.plot(xx, yy)
    plt.title('Laplace, n=' + str(buf_size[i]))

plt.show()
for i in range(len(buf_size)):
    fig, ax = plt.subplots(1, 3)

    x = linspace(-4,4,1000)

    y = laplace.pdf(x)

    ax[0].plot(x, y)
    ax[1].plot(x, y)
    ax[2].plot(x, y)


    x = laplace.rvs(scale=sqrt(1 / 2), size=buf_size[i])
    x = x[x <= 4]
    x = x[x >= -4]
    x.sort()

    kde = gaussian_kde(x)
    kde.set_bandwidth(bw_method='silverman')
    h_n = kde.factor

    sns.kdeplot(x, ax=ax[0], bw=h_n/2)
    sns.kdeplot(x, ax=ax[1], bw=h_n)
    sns.kdeplot(x, ax=ax[2], bw=h_n*2)

    ax[0].set_title(r'$h = \frac{h_n}{2}$')
    ax[1].set_title(r'$h = h_n$')
    ax[2].set_title(r'$h = h_n*2$')

    plt.suptitle('Laplace, n='+ str(buf_size[i]))
    plt.show()

print()
print("---------------------------------------CAUCHY----------------------------------------------------------")

#   CAUCHY

for i in range(len(buf_size)):
    x = linspace(-4, 4, 1000)
    y = cauchy.cdf(x)
    plt.subplot(1, len(buf_size), i + 1)
    plt.plot(x, y)

    y = linspace(0, 1, buf_size[i])
    y.sort()
    x = cauchy.rvs(size=buf_size[i])
    x.sort()

    for j in range(buf_size[i]):
        if x[j] < -4:
            x[j] = -4
        elif x[j] > 4:
            x[j] = 4

    yy = empty(buf_size[i] * 2)
    yy[0] = 0
    yy[1] = y[0]
    for j in range(buf_size[i] - 1):
        yy[j * 2 + 2] = y[j + 1]
        yy[j * 2 + 3] = y[j + 1]

    xx = empty(buf_size[i] * 2)
    xx[0] = -4
    for j in range(buf_size[i] - 1):
        xx[j * 2 + 1] = x[j]
        xx[j * 2 + 2] = x[j]
    xx[buf_size[i] * 2 - 1] = 4

    plt.plot(xx, yy)
    plt.title('Cauchy, n=' + str(buf_size[i]))

plt.show()
for i in range(len(buf_size)):
    fig, ax = plt.subplots(1, 3)

    x = linspace(-4,4,1000)

    y = cauchy.pdf(x)
    ax[0].plot(x,y)
    ax[1].plot(x, y)
    ax[2].plot(x, y)

    x = cauchy.rvs(size=buf_size[i])
    x = x[x <= 4]
    x = x[x >= -4]
    x.sort()

    kde = gaussian_kde(x)
    kde.set_bandwidth(bw_method='silverman')
    h_n = kde.factor

    sns.kdeplot(x, ax=ax[0], bw=h_n/2)
    sns.kdeplot(x, ax=ax[1], bw=h_n)
    sns.kdeplot(x, ax=ax[2], bw=h_n*2)

    ax[0].set_title(r'$h = \frac{h_n}{2}$')
    ax[1].set_title(r'$h = h_n$')
    ax[2].set_title(r'$h = h_n*2$')

    plt.suptitle('Cauchy, n='+ str(buf_size[i]))
    plt.show()

print()
print("---------------------------------------POISSION----------------------------------------------------------")

#   POISSION

for i in range(len(buf_size)):
    x = linspace(6, 14, 1000)
    y = poisson.cdf(x, 10)
    plt.subplot(1, len(buf_size), i + 1)
    plt.plot(x, y)

    y = linspace(0, 1, buf_size[i])
    y.sort()
    x = poisson.rvs(10, size=buf_size[i])
    x.sort()

    for j in range(buf_size[i]):
        if x[j] < 6:
            x[j] = 6
        elif x[j] > 14:
            x[j] = 14

    yy = empty(buf_size[i] * 2)
    yy[0] = 0
    yy[1] = y[0]
    for j in range(buf_size[i] - 1):
        yy[j * 2 + 2] = y[j + 1]
        yy[j * 2 + 3] = y[j + 1]

    xx = empty(buf_size[i] * 2)
    xx[0] = 6
    for j in range(buf_size[i] - 1):
        xx[j * 2 + 1] = x[j]
        xx[j * 2 + 2] = x[j]
    xx[buf_size[i] * 2 - 1] = 14

    plt.plot(xx, yy)
    plt.title('Poisson, n=' + str(buf_size[i]))

plt.show()
for i in range(len(buf_size)):
    fig, ax = plt.subplots(1, 3)

    x = linspace(5, 15, 11)

    y = poisson.pmf(x, 10)

    ax[0].plot(x, y)
    ax[1].plot(x, y)
    ax[2].plot(x, y)

    x = poisson.rvs(10, size=buf_size[i])
    x = x[x <= 14]
    x = x[x >= 6]
    x.sort()

    kde = gaussian_kde(x)
    kde.set_bandwidth(bw_method='silverman')
    h_n = kde.factor

    sns.kdeplot(x, ax=ax[0], bw=h_n/2)
    sns.kdeplot(x, ax=ax[1], bw=h_n)
    sns.kdeplot(x, ax=ax[2], bw=h_n*2)

    ax[0].set_title(r'$h = \frac{h_n}{2}$')
    ax[1].set_title(r'$h = h_n$')
    ax[2].set_title(r'$h = h_n*2$')

    plt.suptitle('Poisson, n='+ str(buf_size[i]))
    plt.show()

print()
print("---------------------------------------UNIFORM----------------------------------------------------------")


#   UNIFORM
for i in range(len(buf_size)):
    x = linspace(-4, 4, 1000)
    y = uniform.cdf(x, -sqrt(3), 2 * sqrt(3))
    plt.subplot(1, len(buf_size), i + 1)
    plt.plot(x, y)

    y = linspace(0, 1, buf_size[i])
    y.sort()
    x = random.uniform(-sqrt(3), sqrt(3), buf_size[i])
    x.sort()

    for j in range(buf_size[i]):
        if x[j] < -4:
            x[j] = -4
        elif x[j] > 4:
            x[j] = 4

    yy = empty(buf_size[i] * 2)
    yy[0] = 0
    yy[1] = y[0]
    for j in range(buf_size[i] - 1):
        yy[j * 2 + 2] = y[j + 1]
        yy[j * 2 + 3] = y[j + 1]

    xx = empty(buf_size[i] * 2)
    xx[0] = -4
    for j in range(buf_size[i] - 1):
        xx[j * 2 + 1] = x[j]
        xx[j * 2 + 2] = x[j]
    xx[buf_size[i] * 2 - 1] = 4

    plt.plot(xx, yy)
    plt.title('Uniform, n=' + str(buf_size[i]))

plt.show()

for i in range(len(buf_size)):
    fig, ax = plt.subplots(1, 3)

    x = linspace(-4, 4, 1000)

    y = uniform.pdf(x, -sqrt(3), 2 * sqrt(3))
    ax[0].plot(x, y)
    ax[1].plot(x, y)
    ax[2].plot(x, y)

    x = random.uniform(-sqrt(3), sqrt(3), buf_size[i])
    x = x[x <= 4]
    x = x[x >= -4]
    x.sort()

    kde = gaussian_kde(x)
    kde.set_bandwidth(bw_method='silverman')
    h_n = kde.factor

    sns.kdeplot(x, ax=ax[0], bw=h_n / 2)
    sns.kdeplot(x, ax=ax[1], bw=h_n)
    sns.kdeplot(x, ax=ax[2], bw=h_n * 2)

    ax[0].set_title(r'$h = \frac{h_n}{2}$')
    ax[1].set_title(r'$h = h_n$')
    ax[2].set_title(r'$h = h_n*2$')

    plt.suptitle('Uniform, n=' + str(buf_size[i]))
    plt.show()

