from pylab import *
from scipy.stats import *
from numpy import random
import matplotlib.pyplot as plt

buf_size = [20,100]

print("---------------------------------------NORMAL----------------------------------------------------------")
# NORMAL
for i in range(len(buf_size)):
    x = norm.rvs(scale=1, size=buf_size[1])

    plt.subplot(1, len(buf_size), i + 1)
    plt.boxplot(x)
    plt.title('Normal, n='+ str(buf_size[i]))

plt.show()


print()
print("---------------------------------------LAPLACE----------------------------------------------------------")
#   LAPLACE
for i in range(len(buf_size)):

    x = laplace.rvs(scale=sqrt(1/2), size=buf_size[i])

    plt.subplot(1, len(buf_size), i + 1)
    plt.boxplot(x)
    plt.title('Laplace, n=' + str(buf_size[i]))

plt.show()


print()
print("---------------------------------------CAUCHY----------------------------------------------------------")

#   CAUCHY

for i in range(len(buf_size)):
    x = cauchy.rvs(size=buf_size[i])

    plt.subplot(1, len(buf_size), i + 1)
    plt.boxplot(x)
    plt.title('Cauchy, n=' + str(buf_size[i]))

plt.show()


print()
print("---------------------------------------POISSION----------------------------------------------------------")

#   POISSION

for i in range(len(buf_size)):
    x = poisson.rvs(10, size=buf_size[i])

    plt.subplot(1, len(buf_size), i + 1)
    plt.boxplot(x)
    plt.title('Poisson, n=' + str(buf_size[i]))

plt.show()


print()
print("---------------------------------------UNIFORM----------------------------------------------------------")


#   UNIFORM
for i in range(len(buf_size)):
    x = random.uniform(-sqrt(3), sqrt(3), buf_size[i])

    plt.subplot(1, len(buf_size), i + 1)
    plt.boxplot(x)
    plt.title('Uniform, n=' + str(buf_size[i]))

plt.show()

