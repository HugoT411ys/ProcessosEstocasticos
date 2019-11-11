import pandas
import numpy
from matplotlib import pyplot

if __name__ == '__main__':
    data = pandas.read_csv('plot.csv', encoding='utf-8')

    n = data['n'].tolist()
    sigma = data['sigma'].tolist()

    pyplot.plot(n[:1000], sigma[:1000], 'r', label='valor simulado')
    x = numpy.linspace(0, 1000)
    pyplot.plot(x, [133/15 for _ in x], '--b', label='valor exato')

    pyplot.legend()

    pyplot.show()

