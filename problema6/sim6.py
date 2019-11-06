import numpy
from matplotlib import pyplot


def brownian_motion(rows, columns):
    x = numpy.random.normal(loc=0., scale=1./columns, size=(rows, columns))
    x[:, 0] = 0.
    return numpy.cumsum(x, axis=1)


def density_func(m):
    return numpy.sqrt(2./numpy.pi) * numpy.exp(-(m**2)/2)


if __name__ == '__main__':
    n, m = 5, 1000

    # Simulating and plotting small sample. Just for visualization.
    brown = brownian_motion(rows=n, columns=m)

    fig1, ax1 = pyplot.subplots()

    for b in brown:
        ax1.plot(b)

    ax1.set(xlabel='i', ylabel='$B_{t_i}$')
    ax1.grid()
    fig1.savefig('brownian.pdf')

    # Simulating and plotting histogram of a bigger sample.
    n = 10000
    brown = brownian_motion(rows=n, columns=m)

    max_brown = numpy.max(brown, axis=1)

    fig2, ax2 = pyplot.subplots()
    ax2.hist(max_brown, alpha=0.3, bins=8, color='b')

    ax2.set(xlabel='$M_1$', ylabel='$freq$')

    fig2.savefig("histogram.pdf")

    # Plotting the exact probability density function
    fig3, ax3 = pyplot.subplots()
    x_values = numpy.linspace(numpy.min(max_brown), numpy.max(max_brown), m)
    ax3.plot(x_values, [density_func(x) for x in x_values],'r')

    ax3.set(xlabel='m', ylabel='$f_{M_1}$')

    fig3.savefig("density.pdf")

    pyplot.show()
