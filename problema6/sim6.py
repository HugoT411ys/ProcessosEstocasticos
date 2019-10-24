import numpy
from matplotlib import pyplot


def brownian_motion(rows, columns):
    x = numpy.random.normal(loc=0., scale=1./columns, size=(rows, columns))
    x[:, 0] = 0.
    return numpy.cumsum(x, axis=1)


def density_func(m):
    return numpy.sqrt(2./numpy.pi) * numpy.exp(-(m**2)/2)


if __name__ == '__main__':
    r, c = 5, 1000

    # Simulating and plotting small sample. Just for visualization.
    brown = brownian_motion(rows=r, columns=c)

    fig1, ax1 = pyplot.subplots()
    fig1.set_size_inches(8, 4)

    for b in brown:
        ax1.plot(b)

    ax1.set(xlabel='i', ylabel='$B_{t_i}$')
    ax1.grid()
    fig1.savefig('brownian.pdf')

    # Simulating and plotting histogram of a bigger sample.
    r = 500
    brown = brownian_motion(rows=r, columns=c)

    max_brown = numpy.max(brown, axis=1)

    fig2, ax2 = pyplot.subplots()
    fig2.set_size_inches(8, 4)
    ax2.hist(max_brown, alpha=0.3, bins=10, color='b')

    ax2.set(xlabel='$M_1$', ylabel='$freq$')

    fig2.savefig("histogram.pdf")

    # Plotting the exact probability density function
    fig3, ax3 = pyplot.subplots()
    fig3.set_size_inches(8, 4)
    x_values = numpy.linspace(numpy.min(max_brown), numpy.max(max_brown), c)
    ax3.plot(x_values, [density_func(x) for x in x_values],'r')

    ax3.set(xlabel='m', ylabel='$f_{M_1}$')

    fig3.savefig("density.pdf")

    pyplot.show()
