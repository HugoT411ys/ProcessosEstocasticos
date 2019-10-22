import numpy
from matplotlib import pyplot


def f(t):
    return numpy.sin(t) + numpy.random.normal(loc=0, scale=0.16)

if __name__ == '__main__':
    X = numpy.linspace(0., 2*numpy.pi, 100)
    Y = [f(x) for x in X]

    fig, ax = pyplot.subplots()

    ax.plot(X, Y, 'r')

    ax.set(xlabel='x', ylabel='$f(x) = sin(x) + \epsilon$', title='Regressão')
    ax.grid()

    fig.savefig("gauss.pdf")
    pyplot.show()