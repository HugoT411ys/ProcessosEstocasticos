import sys
import time
from markov import MarkovChain

N = 1000000


def output_results(s, m):
    print('----------------------------------------------------------------------------------------------------')
    print('Initial state: ' + s)
    print('Limit Distribution: ')
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

    f = open('markov1.txt', 'w')
    sys.stdout = f

    print('====================================================================================================')
    print('Simulating Discrete-Time Markov Chain')
    print('State Space: ')
    print(markov.states)
    print('Number of Iterations: ' + str(N))
    print('====================================================================================================')

    for state in markov.states:
        markov.run(init_state=state, num_iter=N)
        output_results(state, markov)
        markov.reset()

    print('====================================================================================================')
    print("Total execution time: %s seconds." % (time.time() - start_time))
    print('====================================================================================================')
