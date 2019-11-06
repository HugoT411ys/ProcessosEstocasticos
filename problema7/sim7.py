import numpy
from matplotlib import pyplot


def expected_value(scholes, k, r, t):
    plus = numpy.vectorize(lambda x: max(x, 0.))
    big_sigma = plus((scholes[len(scholes)-1, :] - k)).sum()
    return numpy.exp(-r*t) * big_sigma / scholes.shape[0]


def black_scholes(s_zero, r, s, dt, bt):
    return s_zero * numpy.array([[numpy.exp((r - 0.5*s**2)*(t*dt) + w*s) for t, w in enumerate(path)] for path in bt])


if __name__ == '__main__':
    n, m = 100, 1000

    total_time = 1.

    w_t = numpy.random.normal(loc=0., scale=total_time/m, size=(n, m))
    w_t[:,0] = 0.
    w_t = numpy.cumsum(w_t, axis=1)

    s_t = black_scholes(s_zero=100, r=0.05, s=0.4, dt=total_time/m, bt=w_t)

    fig1, ax1 = pyplot.subplots()

    for s in s_t:
        ax1.plot(s)

    ax1.set(xlabel='i', ylabel='$S_{t_i}$')
    ax1.grid()

    fig1.savefig('scholes.pdf')

    fig2, ax2 = pyplot.subplots()

    k = numpy.linspace(start=80, stop=120, num=5)

    c = [expected_value(scholes=s_t, k=i, r=0.05, t=total_time) for i in k]

    ax2.plot(k, c, 'b')

    ax2.set(xlabel='K', ylabel='$C(K)$')
    ax2.grid()

    fig2.savefig('monte_carlo.pdf')

    pyplot.show()
