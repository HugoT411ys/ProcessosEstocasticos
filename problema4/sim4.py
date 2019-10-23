from problema4.poisson_process import PoissonProcess
from matplotlib import pyplot


if __name__ == '__main__':
    J = 5

    poisson = PoissonProcess(total_time=5., rate=1., init_state=0)
    sigma = 0.

    fig, ax = pyplot.subplots()

    for _ in range(J):
        poisson.run()
        n, t = poisson.retrieve_data()
        sigma = sigma + poisson.integral()
        ax.step(t, n, where='post')
        poisson.reset(init_state=0)

    ax.set(xlabel='t', ylabel='$N_t$', title='Processo de Poisson')
    ax.grid()

    fig.savefig("poisson.pdf")
    pyplot.show()

    pyplot.show()
