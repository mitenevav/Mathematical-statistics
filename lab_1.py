from pylab import *
from scipy.stats import *
from numpy import random
###     norm 10
x = norm.rvs(scale = 1,size=10)
x.sort()
#hist(x, 10, density=True, histtype='stepfilled', alpha=0.2)

###     norm 50
x = norm.rvs(scale = 1,size=50)
x.sort()
#hist(x, 15, density=True, histtype='stepfilled', alpha=0.2)

###     norm 1000
x = norm.rvs(scale = 1,size=1000)
x.sort()
#hist(x, 20, density=True, histtype='stepfilled', alpha=0.2)

y=linspace(-3,3,1000)
#plot(y,norm.pdf(y))
#show()




###     laplace 10
x = laplace.rvs(scale = sqrt(1/2),size=10)
x.sort()
#hist(x, 10, density=True, histtype='stepfilled', alpha=0.2)

###     laplace 50
x = laplace.rvs(scale = sqrt(1/2),size=50)
x.sort()
#hist(x, 15, density=True, histtype='stepfilled', alpha=0.2)

###     laplace 1000
x = laplace.rvs(scale = sqrt(1/2),size=1000)
x.sort()
#hist(x, 20, density=True, histtype='stepfilled', alpha=0.2)

y=linspace(-3,3,1000)
#plot(y,laplace.pdf(y))
#show()


###     cauchy 10
x = cauchy.rvs(size=10)
x.sort()
#hist(x, 10, density=True, histtype='stepfilled', alpha=0.2)

###     cauchy 50
x = cauchy.rvs(size=50)
x.sort()
#hist(x, 15, density=True, histtype='stepfilled', alpha=0.2)

###     cauchy 1000
x = cauchy.rvs(size=1000)
x.sort()
#hist(x, 20, density=True, histtype='stepfilled', alpha=0.2)

y=linspace(-3,3,1000)
#plot(y,cauchy.pdf(y))
#show()

###     pos 10

x = poisson.rvs(10,size=10)
x.sort()
#hist(x, 10, density=True, histtype='stepfilled', alpha=0.2)

###     pos 50
x =  poisson.rvs(10,size=50)
x.sort()
#hist(x, 15, density=True, histtype='stepfilled', alpha=0.2)

###     pos 1000
x =  poisson.rvs(10,size=1000)
x.sort()
#hist(x, 20, density=True, histtype='stepfilled', alpha=0.2)

y=linspace(0,20,21)
#plot(y,poisson.pmf(y,10))
#show()


###     ravn 10

x = random.uniform(0, 1, 10)

x.sort()
#hist(x, 10, density=True, histtype='stepfilled', alpha=0.2)

###     ravn 50
x = random.uniform(0, 1, 50)
x.sort()
#hist(x, 15, density=True, histtype='stepfilled', alpha=0.2)

###     ravn 1000
x = random.uniform(0,1,1000)
x.sort()
hist(x, 20, density=True, histtype='stepfilled', alpha=0.2)

y=linspace(0,1,1000)
plot(x, ones_like(x))
show()

