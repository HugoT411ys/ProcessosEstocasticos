import numpy
from matplotlib import pyplot


if __name__ == '__main__':
    rows, columns = 10, 100
    X = numpy.random.normal(loc=0, scale=1./columns, size=(rows, columns))
    X[:, 0] = 0.
    B = numpy.cumsum(X, axis=0)

    M = numpy.max(B, axis=1)

    fig, ax = pyplot.subplots()
    for b in B:
        ax.plot(b)

    ax.set(xlabel='i', ylabel='$B_{t_i}$', title='Movimento Browniano')
    ax.grid()
    fig.set_size_inches(8, 4)
    fig.savefig("browninan.pdf")

    pyplot.show()

    fig, ax = pyplot.subplots()
    ax.hist(M, weights=numpy.zeros_like(M) + 1. / M.size, alpha=0.5, bins=5, color='g')
    x = numpy.linspace(numpy.min(M), numpy.max(M), 5)
    y = [numpy.sqrt(2./numpy.pi) * numpy.exp(-(m**2/2)) for m in x]
    ax.plot(x, y, 'r--', label='$f_{M_1}$')
    ax.legend()

    ax.set(xlabel='$M_1$', ylabel='$freq$', title='Histograma')

    fig.set_size_inches(8, 4)
    fig.savefig("hist.pdf")

    pyplot.show()
