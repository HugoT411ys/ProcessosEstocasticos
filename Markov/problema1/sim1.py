import sys
import time
from Markov.markov import MarkovChain

N = 1000000


def output_results(s, m):
    print('----------------------------------------------------------------------------------------------------')
    print('Estado inicial: ' + s)
    print('Distribuição Limite: ')
    print(m.distribution())
    print('----------------------------------------------------------------------------------------------------')


if __name__ == '__main__':
    start_time = time.time()

    P = {'1': {'1': 1./3, '2': 0., '3': 2./3, '4': 0., '5': 0.},
         '2': {'1': 1./4, '2': 1./2, '3': 1./4, '4': 0., '5': 0.},
         '3': {'1': 1./2, '2': 0., '3': 1./2, '4': 0., '5': 0.},
         '4': {'1': 0., '2': 0., '3': 0., '4': 0., '5': 1.},
         '5': {'1': 0., '2': 0., '3': 0., '4': 2./3, '5': 1./3}}

    markov = MarkovChain(trans_prob=P)

    f = open('sim1_out.txt', 'w')
    sys.stdout = f

    print('====================================================================================================')
    print('Simulando Cadeia de Markov em tempo discreto')
    print('Espaço de estados: ')
    print(markov.states)
    print('Número de iterações: ' + str(N))
    print('====================================================================================================')

    for state in markov.states:
        markov.run(init_state=state, num_iter=N)
        output_results(state, markov)
        markov.reset()

    print('====================================================================================================')
    print("Tempo de execução: %s segundos." % (time.time() - start_time))
    print('====================================================================================================')
