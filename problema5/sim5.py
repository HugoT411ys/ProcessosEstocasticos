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


if __name__ == '__main__':
    n = 1000
    sigma_n2 = 0.16
    x_test = numpy.linspace(-numpy.pi, numpy.pi, n)
    y_test = numpy.sin(x_test) + numpy.random.normal(loc=0., scale=sigma_n2, size=x_test.shape)

    x_train = numpy.linspace(-numpy.pi, numpy.pi, n)

    mean, cov = gpr(x_test, y_test, x_train, sigma_n2)

    # Plot data
    std = numpy.array([numpy.sqrt(x) for x in cov.diagonal()])

    fig, ax = pyplot.subplots()
    pyplot.gca().fill_between(x_train, mean - 2*std, mean + 2*std,
                              color='blue', alpha=0.25)
    ax.scatter(x_test, y_test, s=5, color='red', label='$sin(x) + \\epsilon$')
    ax.plot(numpy.linspace(-numpy.pi, numpy.pi, n), numpy.sin(x_test),label='sin(x)')
    ax.plot(x_train, mean, 'g--', label='$\\mu$')
    ax.set(xlabel='x')
    ax.legend(loc='best')
    pyplot.title('Gaussian Process Regression - Confidence Interval $[\\mu - 2\\sigma, \\mu + 2\\sigma]$')
    ax.grid()
    fig.savefig("gp_regression.pdf")

    manager = pyplot.get_current_fig_manager()
    manager.window.showMaximized()

    pyplot.show()
