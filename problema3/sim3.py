import numpy
from matplotlib import pyplot


if __name__ == '__main__':
    n_iter = 100
    n_sim = 10

    m_val = [1./2, 3./2]
    m_dist = [.5, .5]

    martingale = [[] for _ in range(n_sim)]

    for m in martingale:
        prev = 1
        for _ in range(n_iter):
            prev = numpy.random.choice(m_val, p=m_dist) * prev
            m.append(prev)

    fig, ax = pyplot.subplots()

    for m in martingale:
        ax.plot(m)

    ax.set(xlabel='n', ylabel='$M_n$', title='Martingal')
    ax.grid()

    fig.savefig("martingale.pdf")
    pyplot.show()
