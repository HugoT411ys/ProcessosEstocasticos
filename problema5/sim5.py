import numpy
from matplotlib import pyplot


# https://katbailey.github.io/post/gaussian-processes-for-dummies/


def kernel(rows, cols):
    sigma_f = length = 1.
    k = numpy.array([[(i - j)**2 for j in cols] for i in rows])
    k = sigma_f**2 * numpy.exp((-0.5/length**2) * k)
    return k


def gpr(x, y, xs, var):
    kxx = kernel(x, x)
    kxs = kernel(x, xs)
    ksx = kernel(xs, x)
    kss = kernel(xs, xs)

    temp = numpy.linalg.inv(kxx + var * numpy.eye(kxx.shape[0]))

    m = (ksx.dot(temp)).dot(y)
    c = kss + var * numpy.eye(kss.shape[0]) - (ksx.dot(temp)).dot(kxs)

    return m, c


def main():
    n, ns = 5, 50
    I = (-numpy.pi, numpy.pi)

    sig = 0.4  # sig**2 = 0.16
    sig = 0.
    x = numpy.linspace(I[0], I[1], n)
    y = numpy.sin(x) + numpy.random.normal(loc=0., scale=sig, size=x.shape)

    xs = numpy.linspace(I[0], I[1], ns)

    mean, cov = gpr(x, y, xs, sig**2)

    # Plot data
    std = numpy.array([numpy.sqrt(x) for x in cov.diagonal()])

    fig, ax = pyplot.subplots()
    pyplot.gca().fill_between(xs, mean - 2 * std, mean + 2 * std, color='blue', alpha=0.25)

    ax.scatter(x, y, s=15, color='red', label='$sin(x) + \\epsilon$')
    ax.plot(xs, mean, 'g--', label='$\\mu$')
    ax.plot(xs, numpy.sin(xs), 'y', label="$sin(x)$")
    ax.set(xlabel='x')
    ax.legend(loc='best')
    ax.grid()
    fig.savefig("gp_regression0.pdf")

    pyplot.show()


if __name__ == '__main__':
    main()
