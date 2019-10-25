import sys

from stochastic import PoissonProcess
from matplotlib import pyplot


if __name__ == '__main__':
    num_sim = 50
    sigma_exp = 0.
    sigma_uni = 0.

    p = PoissonProcess(total_time=5., rate=1., init_state=0)

    fig, ax = pyplot.subplots()

    for _ in range(num_sim):
        p.simulate_exponential()
        sigma_exp = sigma_exp + p.integral()
        t_exp, N_exp = p.retrieve_data()
        ax.step(t_exp, N_exp, where='post')
        p.reset(init_state=0)

    ax.set(xlabel='t', ylabel='$N_t$')
    ax.grid()

    fig.savefig("poisson_exp.pdf")
    pyplot.show()

    fig, ax = pyplot.subplots()

    for _ in range(num_sim):
        p.simulate_uniform()
        sigma_uni = sigma_uni + p.integral()
        t_uni, N_uni = p.retrieve_data()
        ax.step(t_uni, N_uni, where='post')
        p.reset(init_state=0)

    ax.set(xlabel='t', ylabel='$N_t$')
    ax.grid()

    fig.savefig("poisson_uni.pdf")
    pyplot.show()
    f = open('sim4_out.txt', 'w')
    sys.stdout = f

    print('====================================================================================================')
    print('Simulando Processo de Poisson')
    print('Quantidade de caminhos (J): ' + str(num_sim))
    print('Valor aproximado para esperança da integral: ')
    print('Simulação exponencial: ' + 'E ~ ' + str(sigma_exp / num_sim))
    print('Simulação uniforme: ' + 'E ~ ' + str(sigma_uni / num_sim))
    print('====================================================================================================')
