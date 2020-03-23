from pylab import *
from scipy.stats import *
from numpy import random
import matplotlib.pyplot as plt

buf_size = [20,100]

print("---------------------------------------NORMAL----------------------------------------------------------")
# NORMAL
for i in range(len(buf_size)):
    x = norm.rvs(scale=1, size=buf_size[i])

    plt.subplot(1, len(buf_size), i + 1)
    plt.boxplot(x)
    plt.title('Normal, n='+ str(buf_size[i]))

    less = 0
    more = 0

    for j in range(1000):
        x = norm.rvs(scale=1, size=buf_size[i])
        x.sort()

        zp1 = x[int(buf_size[i] / 4)]
        zp3 = x[int(buf_size[i] * 3 / 4)]

        x_down = zp1 - 1.5 * (zp3-zp1)
        x_up = zp3 + 1.5 * (zp3-zp1)

        less += len(x[x < x_down]) / buf_size[i]
        more += len(x[x > x_up]) / buf_size[i]

    print(f"NORMAL, n = {buf_size[i]}")

    print(less / 1000)
    print(more / 1000)

    print(more / 1000 + less / 1000)

plt.show()


print()
print("---------------------------------------LAPLACE----------------------------------------------------------")
#   LAPLACE
for i in range(len(buf_size)):

    x = laplace.rvs(scale=sqrt(1/2), size=buf_size[i])


    plt.subplot(1, len(buf_size), i + 1)
    plt.boxplot(x)
    plt.title('Laplace, n=' + str(buf_size[i]))


    less = 0
    more = 0

    for j in range(1000):
        x = laplace.rvs(scale=sqrt(1 / 2), size=buf_size[i])
        x.sort()

        zp1 = x[int(buf_size[i] / 4)]
        zp3 = x[int(buf_size[i] * 3 / 4)]

        x_down = zp1 - 1.5 * (zp3-zp1)
        x_up = zp3 + 1.5 * (zp3-zp1)

        less += len(x[x < x_down]) / buf_size[i]
        more += len(x[x > x_up]) / buf_size[i]

    print(f"Laplace, n = {buf_size[i]}")

    print(less / 1000)
    print(more / 1000)

    print(more / 1000 + less / 1000)

plt.show()


print()
print("---------------------------------------CAUCHY----------------------------------------------------------")

#   CAUCHY

for i in range(len(buf_size)):
    x = cauchy.rvs(size=buf_size[i])


    plt.subplot(1, len(buf_size), i + 1)
    plt.boxplot(x)
    plt.title('Cauchy, n=' + str(buf_size[i]))


    less = 0
    more = 0

    for j in range(1000):
        x = cauchy.rvs(size=buf_size[i])
        x.sort()

        zp1 = x[int(buf_size[i] / 4)]
        zp3 = x[int(buf_size[i] * 3 / 4)]

        x_down = zp1 - 1.5 * (zp3-zp1)
        x_up = zp3 + 1.5 * (zp3-zp1)

        less += len(x[x < x_down]) / buf_size[i]
        more += len(x[x > x_up]) / buf_size[i]

    print(f"Cauchy, n = {buf_size[i]}")

    print(less / 1000)
    print(more / 1000)

    print(more / 1000 + less / 1000)

plt.show()


print()
print("---------------------------------------POISSION----------------------------------------------------------")

#   POISSION

for i in range(len(buf_size)):
    x = poisson.rvs(10, size=buf_size[i])

    plt.subplot(1, len(buf_size), i + 1)
    plt.boxplot(x)
    plt.title('Poisson, n=' + str(buf_size[i]))


    less = 0
    more = 0

    for j in range(1000):
        x = poisson.rvs(10, size=buf_size[i])
        x.sort()

        zp1 = x[int(buf_size[i] / 4)]
        zp3 = x[int(buf_size[i] * 3 / 4)]

        x_down = zp1 - 1.5 * (zp3-zp1)
        x_up = zp3 + 1.5 * (zp3-zp1)

        less += len(x[x < x_down]) / buf_size[i]
        more += len(x[x > x_up]) / buf_size[i]

    print(f"poission, n = {buf_size[i]}")

    print(less / 1000)
    print(more / 1000)

    print(more / 1000 + less / 1000)

plt.show()


print()
print("---------------------------------------UNIFORM----------------------------------------------------------")


#   UNIFORM
for i in range(len(buf_size)):
    x = random.uniform(-sqrt(3), sqrt(3), buf_size[i])


    plt.subplot(1, len(buf_size), i + 1)
    plt.boxplot(x)
    plt.title('Uniform, n=' + str(buf_size[i]))


    less = 0
    more = 0

    for j in range(1000):
        x = random.uniform(-sqrt(3), sqrt(3), buf_size[i])
        x.sort()

        zp1 = x[int(buf_size[i] / 4)]
        zp3 = x[int(buf_size[i] * 3 / 4)]

        x_down = zp1 - 1.5 * (zp3-zp1)
        x_up = zp3 + 1.5 * (zp3-zp1)

        less += len(x[x < x_down]) / buf_size[i]
        more += len(x[x > x_up]) / buf_size[i]

    print(f"Uniform, n = {buf_size[i]}")

    print(less / 1000)
    print(more / 1000)

    print(more / 1000 + less / 1000)

plt.show()

