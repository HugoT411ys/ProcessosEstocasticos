import pandas
import numpy
from matplotlib import pyplot

if __name__ == '__main__':
    data = pandas.read_csv('poisson_exp.csv', encoding='UTF-16LE')

    n = data['n'].tolist()
    sigma = data['sigma'].tolist()

    pyplot.plot(n, sigma, 'r', label='valor simulado')
    x = numpy.linspace(-100000, 100000)
    pyplot.plot(x, [12.5 for _ in x], '--b', label='valor exato')

    pyplot.yticks(numpy.arange(7, 17, step=0.5))

    pyplot.xlim(-1000, 11000)

    pyplot.legend()
    pyplot.show()

