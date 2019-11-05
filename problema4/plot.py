import pandas
from matplotlib import pyplot

if __name__ == '__main__':
    data=pandas.read_csv('poisson_uni.csv', encoding='UTF-16LE')

    n=data['n'].tolist()
    sigma=data['sigma'].tolist()

    pyplot.plot(n, sigma, 'r')
    pyplot.plot(n, [12.5 for _ in n], '--b')
    pyplot.show()

