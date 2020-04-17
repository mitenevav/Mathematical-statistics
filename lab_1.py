import seaborn as sns
from matplotlib import transforms
from matplotlib.patches import Ellipse
from pylab import *
from scipy.stats import *
from numpy import random
from matplotlib import*
import matplotlib.pyplot as plt
import numpy as np



def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of `x` and `y`

    Parameters
    ----------
    x, y : array_like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    Returns
    -------
    matplotlib.patches.Ellipse

    Other parameters
    ----------------
    kwargs : `~matplotlib.patches.Patch` properties
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensionl dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0),
        width=ell_radius_x * 2,
        height=ell_radius_y * 2,
        facecolor=facecolor,
        **kwargs)

    # Calculating the stdandard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the stdandard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)


buf_size = [20, 60, 100]
ro = [0, 0.5, 0.9]
print("---------------------------------------NORMAL----------------------------------------------------------")
# NORMAL

for k in range(len(ro)):
    for i in range(len(buf_size)):
        r = []
        rs = []
        rq = []
        rv_mean = [0, 0]
        for l in range(1000):
            rv_cov = [[1.0, ro[k]], [ro[k], 1.0]]
            rv = multivariate_normal.rvs(rv_mean, rv_cov, size=buf_size[i])
            x = rv[:, 0]
            y = rv[:, 1]

            r1, t =stats.pearsonr(x, y)
            r.append(r1)

            rs1, t = stats.spearmanr(x,y)
            rs.append(rs1)

            medx = mean(x)
            medy = mean(y)

            n1 = 0
            n2 = 0
            n3 = 0
            n4 = 0

            x0 = x - medx
            y0 = y - medy
            for j in range(buf_size[i]):
                if x0[j] > 0 and y0[j] > 0:
                    n1 += 1
                elif x0[j] < 0 and y0[j] > 0:
                    n2 += 1
                elif x0[j] < 0 and y0[j] < 0:
                    n3 += 1
                elif x0[j] > 0 and y0[j] < 0:
                    n4 += 1

            rq.append( ((float)((n1+n3)-(n2+n4))) / buf_size[i])

        print(buf_size[i], ro[k])

        print("E(z)")
        print("r = ", mean(r))
        print("rs = ", mean(rs))
        print("rq = ", mean(rq))

        print("E(z^2)")
        print("r = ", mean(square(r)))
        print("rs = ", mean(square(rs)))
        print("rq = ", mean(square(rq)))

        print("D(z)")
        print("r = ", std(r)*std(r))
        print("rs = ", std(rs)*std(rs))
        print("rq = ", std(rq) * std(rq))
        print()

for i in range(len(buf_size)):
    fig, ax = plt.subplots(1, 3)
    for k in range(len(ro)):
        rv_cov = [[1.0, ro[k]], [ro[k], 1.0]]
        rv = multivariate_normal.rvs(rv_mean, rv_cov, size=buf_size[i])
        x = rv[:, 0]
        y = rv[:, 1]
        ax[k].scatter(x, y, s=3)
        ax[k].set_title(r'$\rho = $' +str(ro[k]))
        confidence_ellipse(x,y, ax[k], edgecolor='gray')



    plt.show()


print("---------------------------------------NORMAL-COMBO----------------------------------------------------------")
for i in range(len(buf_size)):
    r = []
    rs = []
    rq = []
    rv_mean = [0, 0]
    for l in range(1000):
        rv_cov1 = [[1.0, 0.9], [0.9, 1.0]]
        rv_cov2 = [[10, -0.9], [-0.9, 10]]
        rv = 0.9 * multivariate_normal.rvs(rv_mean, rv_cov1, size=buf_size[i]) + 0.1 * multivariate_normal.rvs(rv_mean, rv_cov2, size=buf_size[i])

        x = rv[:, 0]
        y = rv[:, 1]

        r.append(stats.pearsonr(x, y))
        rs.append(stats.spearmanr(x, y))

        medx = mean(x)
        medy = mean(y)

        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0

        x0 = x - medx
        y0 = y - medy
        for j in range(buf_size[i]):
            if x0[j] > 0 and y0[j] > 0:
                n1 += 1
            elif x0[j] < 0 and y0[j] > 0:
                n2 += 1
            elif x0[j] < 0 and y0[j] < 0:
                n3 += 1
            elif x0[j] > 0 and y0[j] < 0:
                n4 += 1

        rq.append( ((float)((n1+n3)-(n2+n4))) / buf_size[i])
    print(buf_size[i], ro[k])

    print("E(z)")
    print("r = ", mean(r))
    print("rs = ", mean(rs))
    print("rq = ", mean(rq))

    print("E(z^2)")
    print("r = ", mean(square(r)))
    print("rs = ", mean(square(rs)))
    print("rq = ", mean(square(rq)))

    print("D(z)")
    print("r = ", std(r) * std(r))
    print("rs = ", std(rs) * std(rs))
    print("rq = ", std(rq) * std(rq))
    print()