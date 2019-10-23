import numpy
from matplotlib import pyplot


def integral(n, t):
    i = 0
    for j, time in enumerate(t):
        if j != 0:
            i = i + (t[j] - t[j - 1]) * n[j - 1]
    return i


def simulate_uniform(total_arrivals):
    return sorted([numpy.random.uniform() for _ in range(total_arrivals)]), [i for i in range(total_arrivals)]


if __name__ == '__main__':
    J = 10

    fig, ax = pyplot.subplots()

    sigma = 0
    for _ in range(J):
        t, n = simulate_uniform(total_arrivals=5)
        t.append(5.), n.append(5)
        sigma = sigma + integral(n, t)
        ax.step(t, n, where='post')

    sigma = float(sigma / J)
    print(sigma)

    ax.set(xlabel='t', ylabel='$N_t$', title='Processo de Poisson')
    ax.grid()

    fig.savefig("poisson.pdf")
    pyplot.show()

    pyplot.show()