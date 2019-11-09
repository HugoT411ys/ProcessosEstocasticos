import numpy

from matplotlib import pyplot


def main():
    num_states = 5
    num_paths, num_iter = 10, 100
    states = [i for i in range(num_states)]

    tran_prob = numpy.array([
        [1./3, 0., 2./3, 0., 0.],
        [1./4, 1./2, 1./4, 0., 0.],
        [1./2, 0., 1./2, 0., 0.],
        [0., 0., 0., 0., 1.],
        [0., 0., 0., 2./3, 1./3]
    ])

    x_n = numpy.zeros(shape=(num_paths, num_iter))

    for j in range(num_paths):
        cur_state = numpy.random.choice(states)
        for i in range(num_iter):
            x_n[j][i] = cur_state
            cur_state = numpy.random.choice(states, p=tran_prob[cur_state])

    fig, ax = pyplot.subplots()

    for path in x_n:
        ax.plot(numpy.arange(0., num_iter, 1), path)

    ax.set(xlabel='$n$', ylabel='$X_{n}$')

    ax.grid()
    fig.savefig("markov_paths.pdf")

    pyplot.show()


if __name__ == '__main__':
    main()
