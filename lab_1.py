from pylab import *
from scipy.stats import *
from numpy import random
import matplotlib.pyplot as plt

buf_size =[10,50,1000]
size_columns=[10,15,20]

# NORMAL
for i in range(len(buf_size)):
    plt.subplot(1,len(buf_size), i+1)
    x = norm.rvs(scale = 1,size=buf_size[i])
    plt.hist(x, size_columns[i], density=True, histtype='stepfilled', alpha=0.2)
    y = linspace(-3, 3, 1000)
    plt.plot(y,norm.pdf(y))
    plt.xlabel("n="+ str(buf_size[i]))
    plt.ylabel("Плотность распределения")
plt.title("Нормальное распределение")
plt.show()


#   LAPLACE
plt.figure()
for i in range(len(buf_size)):
    plt.subplot(1,len(buf_size), i+1)
    x =  laplace.rvs(scale = sqrt(1/2),size=buf_size[i])
    plt.hist(x, size_columns[i], density=True, histtype='stepfilled', alpha=0.2)
    y = linspace(-3, 3, 1000)
    plt.plot(y,laplace.pdf(y))
    plt.xlabel("n="+ str(buf_size[i]))
    plt.ylabel("Плотность распределения")
plt.title("Распределение Лапласа")
plt.show()

#   CAUCHY
plt.figure()
for i in range(len(buf_size)):
    plt.subplot(1,len(buf_size), i+1)
    x = cauchy.rvs(size=buf_size[i])
    plt.hist(x, size_columns[i], density=True, histtype='stepfilled', alpha=0.2)
    y = linspace(-3, 3, 1000)
    plt.plot(y,cauchy.pdf(y))
    plt.xlabel("n="+ str(buf_size[i]))
    plt.ylabel("Плотность распределения")
plt.title("Распределение Коши")
plt.show()

#   POISSION
plt.figure()
for i in range(len(buf_size)):
    plt.subplot(1,len(buf_size), i+1)
    x = poisson.rvs(10, size=buf_size[i])
    plt.hist(x, size_columns[i], density=True, histtype='stepfilled', alpha=0.2)
    y=linspace(0,20,21)
    plt.plot(y,poisson.pmf(y, 10))
    plt.xlabel("n="+ str(buf_size[i]))
    plt.ylabel("Плотность распределения")
plt.title("Распределение Пуассона")
plt.show()


#   UNIFORM
plt.figure()
for i in range(len(buf_size)):
    plt.subplot(1,len(buf_size), i+1)
    x = random.uniform(0, 1, buf_size[i])
    plt.hist(x, size_columns[i], density=True, histtype='stepfilled', alpha=0.2)
    y = linspace(0, 1, 2)
    plot(y, ones_like(y))
    plt.xlabel("n="+ str(buf_size[i]))
    plt.ylabel("Плотность распределения")
plt.title("Равномерное распределение")
plt.show()