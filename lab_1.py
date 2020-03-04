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
    plt.hist(x, size_columns[i], density=True, histtype='stepfilled', alpha=0.5)
    y = linspace(-3, 3, 1000)
    plt.plot(y,norm.pdf(y))
    plt.xlabel("n="+ str(buf_size[i]))
    plt.ylabel("Плотность распределения")
plt.title("Нормальное распределение")
plt.show()


#   LAPLACE
plt.figure()
c_lim=[3,5,10]
for i in range(len(buf_size)):
    plt.subplot(1,len(buf_size), i+1)
    x =  laplace.rvs(scale = sqrt(1/2),size=buf_size[i])
    plt.hist(x, size_columns[i], density=True, histtype='stepfilled', alpha=0.5)
    y = linspace(-c_lim[i], c_lim[i], 1000)
    plt.plot(y,laplace.pdf(y))
    plt.xlabel("n="+ str(buf_size[i]))
    plt.ylabel("Плотность распределения")
plt.title("Распределение Лапласа")
plt.show()


c_col=[15, 30, 500]
c_lim=[10,20,50]
#   CAUCHY
plt.figure()
for i in range(len(buf_size)):
    plt.subplot(1,len(buf_size), i+1)
    x = cauchy.rvs(size=buf_size[i])
    plt.hist(x, c_col[i], density=True, histtype='stepfilled', alpha=0.5)
    y = linspace(-c_lim[i], c_lim[i], 1000)
    plt.plot(y,cauchy.pdf(y))
    plt.xlabel("n="+ str(buf_size[i]))
    plt.ylabel("Плотность распределения")
    plt.xlim(-c_lim[i], c_lim[i])
plt.title("Распределение Коши")
plt.show()

#   POISSION
plt.figure()

c_lim=[20,20,30]
for i in range(len(buf_size)):
    plt.subplot(1,len(buf_size), i+1)
    x = poisson.rvs(10, size=buf_size[i])
    plt.hist(x, size_columns[i], density=True, histtype='stepfilled', alpha=0.5)
    y=linspace(0,c_lim[i],c_lim[i]+1)
    plt.plot(y,poisson.pmf(y, 10))
    plt.xlabel("n="+ str(buf_size[i]))
    plt.ylabel("Плотность распределения")
plt.title("Распределение Пуассона")
plt.show()


#   UNIFORM
plt.figure()
for i in range(len(buf_size)):
    plt.subplot(1,len(buf_size), i+1)
    x = random.uniform(-sqrt(3), sqrt(3), buf_size[i])
    plt.hist(x, size_columns[i], density=True, histtype='stepfilled', alpha=0.5)
    y = linspace(-sqrt(3), sqrt(3), 2)
    yy = [1/2/sqrt(3), 1/2/sqrt(3)]
    plot(y, yy)
    plt.xlabel("n="+ str(buf_size[i]))
    plt.ylabel("Плотность распределения")
plt.title("Равномерное распределение")
plt.show()