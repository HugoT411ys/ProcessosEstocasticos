import sys
import time
from Markov.markov import MarkovChain

N = 1000000


if __name__ == '__main__':
    start_time = time.time()

    P = {'1': {'1': 1./3, '2': 0., '3': 2./3, '4': 0.},
         '2': {'1': 1./4, '2': 1./2, '3': 1./4, '4': 0.},
         '3': {'1': 1./2, '2': 0., '3': 1./2, '4': 0.},
         '4': {'1': 0., '2': 1./3, '3': 0., '4': 2./3}}

    markov = MarkovChain(trans_prob=P)

    f = open('sim2_out.txt', 'w')
    sys.stdout = f

    print('====================================================================================================')
    print('Simulating Discrete-Time Markov Chain')
    print('State Space: ')
    print(markov.states)
    print('Number of Iterations: ' + str(N))
    print('====================================================================================================')

    sigma = markov.run(init_state='1', num_iter=N)
    print('Limit Approximation: ' + str(sigma))

    print('====================================================================================================')
    print("Total execution time: %s seconds." % (time.time() - start_time))
    print('====================================================================================================')