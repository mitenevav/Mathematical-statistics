from pylab import *
from scipy.stats import *
from numpy import random
import matplotlib.pyplot as plt

buf_size = [10,100,1000]



# NORMAL
for i in range(len(buf_size)):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0

    sum21 = 0
    sum22 = 0
    sum23 = 0
    sum24 = 0
    sum25 = 0


    print()
    print("NORMAL", end=" ")
    print(buf_size[i])

    for k in range(1000):
        x1 = 0
        med = 0
        zR = 0
        zp1 = 0
        zp3 = 0
        zQ = 0
        ztr = 0


        x = norm.rvs(scale = 1,size=buf_size[i])

        for j in range(buf_size[i]):
            x1 += x[j]
        x1 /= buf_size[i]

        sum1 += x1
        sum21 += x1*x1

        med = (x[int(buf_size[i] / 2 - 1)] + x[int(buf_size[i] / 2)]) / 2
        sum2 += med
        sum22 += med*med

        zR = (x[0] + x[buf_size[i]-1])/2
        sum3 += zR
        sum23 += zR*zR


        if i==0:
            zp1 = x[int(buf_size[i] / 4) + 1]
            zp3 = x[int(buf_size[i] * 3 / 4) + 1]
        else:
            zp1 = x[int(buf_size[i] / 4)]
            zp3 = x[int(buf_size[i] * 3 / 4)]
        zQ = (zp1 + zp3) / 2
        sum4 += zQ
        sum24 += zQ*zQ


        r = int(buf_size[i] / 4)
        for j in range(r+1, buf_size[i] - r):
            ztr += x[j]
        ztr /= (buf_size[i] - 2*r)
        sum5 += ztr
        sum25 += ztr*ztr

    sum1 /= 1000
    sum2 /= 1000
    sum3 /= 1000
    sum4 /= 1000
    sum5 /= 1000

    sum21 /= 1000
    sum22 /= 1000
    sum23 /= 1000
    sum24 /= 1000
    sum25 /= 1000

    sum21 -= sum1*sum1
    sum22 -= sum2*sum2
    sum23 -= sum3*sum3
    sum24 -= sum4*sum4
    sum25 -= sum5*sum5

    print("x1 =", sum1)
    print("med =", sum2)
    print("zR =", sum3)
    print("zQ =", sum4)
    print("ztr =", sum5)
    print()
    print("D x1 =", sum21)
    print("D med =", sum22)
    print("D zR =", sum23)
    print("D zQ =", sum24)
    print("D ztr =", sum25)

print()
print("---------------------------------------LAPLACE----------------------------------------------------------")
#   LAPLACE
for i in range(len(buf_size)):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0


    sum21 = 0
    sum22 = 0
    sum23 = 0
    sum24 = 0
    sum25 = 0


    print()
    print("LAPLACE", end=" ")
    print(buf_size[i])

    for k in range(1000):
        x1 = 0
        med = 0
        zR = 0
        zp1 = 0
        zp3 = 0
        zQ = 0
        ztr = 0

        x =  laplace.rvs(scale = sqrt(1/2),size=buf_size[i])

        for j in range(buf_size[i]):
            x1 += x[j]
        x1 /= buf_size[i]

        sum1 += x1
        sum21 += x1 * x1

        med = (x[int(buf_size[i] / 2 - 1)] + x[int(buf_size[i] / 2)]) / 2
        sum2 += med
        sum22 += med * med

        zR = (x[0] + x[buf_size[i] - 1]) / 2
        sum3 += zR
        sum23 += zR * zR

        if i == 0:
            zp1 = x[int(buf_size[i] / 4) + 1]
            zp3 = x[int(buf_size[i] * 3 / 4) + 1]
        else:
            zp1 = x[int(buf_size[i] / 4)]
            zp3 = x[int(buf_size[i] * 3 / 4)]
        zQ = (zp1 + zp3) / 2
        sum4 += zQ
        sum24 += zQ * zQ

        r = int(buf_size[i] / 4)
        for j in range(r + 1, buf_size[i] - r):
            ztr += x[j]
        ztr /= (buf_size[i] - 2 * r)
        sum5 += ztr
        sum25 += ztr * ztr

    sum1 /= 1000
    sum2 /= 1000
    sum3 /= 1000
    sum4 /= 1000
    sum5 /= 1000

    sum21 /= 1000
    sum22 /= 1000
    sum23 /= 1000
    sum24 /= 1000
    sum25 /= 1000

    sum21 -= sum1 * sum1
    sum22 -= sum2 * sum2
    sum23 -= sum3 * sum3
    sum24 -= sum4 * sum4
    sum25 -= sum5 * sum5

    print("x1 =", sum1)
    print("med =", sum2)
    print("zR =", sum3)
    print("zQ =", sum4)
    print("ztr =", sum5)
    print()
    print("D x1 =", sum21)
    print("D med =", sum22)
    print("D zR =", sum23)
    print("D zQ =", sum24)
    print("D ztr =", sum25)
print()
print("---------------------------------------CAUCHY----------------------------------------------------------")

#   CAUCHY

for i in range(len(buf_size)):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0

    sum21 = 0
    sum22 = 0
    sum23 = 0
    sum24 = 0
    sum25 = 0

    print()
    print("CAUCHY", end=" ")
    print(buf_size[i])

    for k in range(1000):
        x1 = 0
        med = 0
        zR = 0
        zp1 = 0
        zp3 = 0
        zQ = 0
        ztr = 0


        x = cauchy.rvs(size=buf_size[i])

        for j in range(buf_size[i]):
            x1 += x[j]
        x1 /= buf_size[i]

        sum1 += x1
        sum21 += x1 * x1

        med = (x[int(buf_size[i] / 2 - 1)] + x[int(buf_size[i] / 2)]) / 2
        sum2 += med
        sum22 += med * med

        zR = (x[0] + x[buf_size[i] - 1]) / 2
        sum3 += zR
        sum23 += zR * zR

        if i == 0:
            zp1 = x[int(buf_size[i] / 4) + 1]
            zp3 = x[int(buf_size[i] * 3 / 4) + 1]
        else:
            zp1 = x[int(buf_size[i] / 4)]
            zp3 = x[int(buf_size[i] * 3 / 4)]
        zQ = (zp1 + zp3) / 2
        sum4 += zQ
        sum24 += zQ * zQ

        r = int(buf_size[i] / 4)
        for j in range(r + 1, buf_size[i] - r):
            ztr += x[j]
        ztr /= (buf_size[i] - 2 * r)
        sum5 += ztr
        sum25 += ztr * ztr

    sum1 /= 1000
    sum2 /= 1000
    sum3 /= 1000
    sum4 /= 1000
    sum5 /= 1000

    sum21 /= 1000
    sum22 /= 1000
    sum23 /= 1000
    sum24 /= 1000
    sum25 /= 1000

    sum21 -= sum1 * sum1
    sum22 -= sum2 * sum2
    sum23 -= sum3 * sum3
    sum24 -= sum4 * sum4
    sum25 -= sum5 * sum5

    print("x1 =", sum1)
    print("med =", sum2)
    print("zR =", sum3)
    print("zQ =", sum4)
    print("ztr =", sum5)
    print()
    print("D x1 =", sum21)
    print("D med =", sum22)
    print("D zR =", sum23)
    print("D zQ =", sum24)
    print("D ztr =", sum25)
print()
print("---------------------------------------POISSION----------------------------------------------------------")

#   POISSION

for i in range(len(buf_size)):

    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0

    sum21 = 0
    sum22 = 0
    sum23 = 0
    sum24 = 0
    sum25 = 0

    print()
    print("POISSION", end=" ")
    print(buf_size[i])

    for k in range(1000):
        x1 = 0
        med = 0
        zR = 0
        zp1 = 0
        zp3 = 0
        zQ = 0
        ztr = 0

        x = poisson.rvs(10, size=buf_size[i])

        for j in range(buf_size[i]):
            x1 += x[j]
        x1 /= buf_size[i]

        sum1 += x1
        sum21 += x1 * x1

        med = (x[int(buf_size[i] / 2 - 1)] + x[int(buf_size[i] / 2)]) / 2
        sum2 += med
        sum22 += med * med

        zR = (x[0] + x[buf_size[i] - 1]) / 2
        sum3 += zR
        sum23 += zR * zR

        if i == 0:
            zp1 = x[int(buf_size[i] / 4) + 1]
            zp3 = x[int(buf_size[i] * 3 / 4) + 1]
        else:
            zp1 = x[int(buf_size[i] / 4)]
            zp3 = x[int(buf_size[i] * 3 / 4)]
        zQ = (zp1 + zp3) / 2
        sum4 += zQ
        sum24 += zQ * zQ

        r = int(buf_size[i] / 4)
        for j in range(r + 1, buf_size[i] - r):
            ztr += x[j]
        ztr /= (buf_size[i] - 2 * r)
        sum5 += ztr
        sum25 += ztr * ztr

    sum1 /= 1000
    sum2 /= 1000
    sum3 /= 1000
    sum4 /= 1000
    sum5 /= 1000

    sum21 /= 1000
    sum22 /= 1000
    sum23 /= 1000
    sum24 /= 1000
    sum25 /= 1000

    sum21 -= sum1 * sum1
    sum22 -= sum2 * sum2
    sum23 -= sum3 * sum3
    sum24 -= sum4 * sum4
    sum25 -= sum5 * sum5

    print("x1 =", sum1)
    print("med =", sum2)
    print("zR =", sum3)
    print("zQ =", sum4)
    print("ztr =", sum5)
    print()
    print("D x1 =", sum21)
    print("D med =", sum22)
    print("D zR =", sum23)
    print("D zQ =", sum24)
    print("D ztr =", sum25)


print()
print("---------------------------------------UNIFORM----------------------------------------------------------")


#   UNIFORM
for i in range(len(buf_size)):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0

    sum21 = 0
    sum22 = 0
    sum23 = 0
    sum24 = 0
    sum25 = 0

    print()
    print("UNIFORM", end=" ")
    print(buf_size[i])

    for k in range(1000):
        x1 = 0
        med = 0
        zR = 0
        zp1 = 0
        zp3 = 0
        zQ = 0
        ztr = 0

        x = random.uniform(-sqrt(3), sqrt(3), buf_size[i])

        for j in range(buf_size[i]):
            x1 += x[j]
        x1 /= buf_size[i]

        sum1 += x1
        sum21 += x1 * x1

        med = (x[int(buf_size[i] / 2 - 1)] + x[int(buf_size[i] / 2)]) / 2
        sum2 += med
        sum22 += med * med

        zR = (x[0] + x[buf_size[i] - 1]) / 2
        sum3 += zR
        sum23 += zR * zR

        if i == 0:
            zp1 = x[int(buf_size[i] / 4) + 1]
            zp3 = x[int(buf_size[i] * 3 / 4) + 1]
        else:
            zp1 = x[int(buf_size[i] / 4)]
            zp3 = x[int(buf_size[i] * 3 / 4)]
        zQ = (zp1 + zp3) / 2
        sum4 += zQ
        sum24 += zQ * zQ

        r = int(buf_size[i] / 4)
        for j in range(r + 1, buf_size[i] - r):
            ztr += x[j]
        ztr /= (buf_size[i] - 2 * r)
        sum5 += ztr
        sum25 += ztr * ztr

    sum1 /= 1000
    sum2 /= 1000
    sum3 /= 1000
    sum4 /= 1000
    sum5 /= 1000

    sum21 /= 1000
    sum22 /= 1000
    sum23 /= 1000
    sum24 /= 1000
    sum25 /= 1000

    sum21 -= sum1 * sum1
    sum22 -= sum2 * sum2
    sum23 -= sum3 * sum3
    sum24 -= sum4 * sum4
    sum25 -= sum5 * sum5

    print("x1 =", sum1)
    print("med =", sum2)
    print("zR =", sum3)
    print("zQ =", sum4)
    print("ztr =", sum5)
    print()
    print("D x1 =", sum21)
    print("D med =", sum22)
    print("D zR =", sum23)
    print("D zQ =", sum24)
    print("D ztr =", sum25)

