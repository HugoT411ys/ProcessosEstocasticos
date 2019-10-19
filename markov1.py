import sys
import numpy


def markov_simulate(init_state, stochastic_matrix, num_it):
    init_dist = numpy.zeros((1, 5))
    init_dist[0][init_state] = 1.

    next_dist = numpy.zeros_like(init_dist)

    for it in range(num_it):
        next_dist = init_dist.dot(stochastic_matrix)
        init_dist = next_dist

    print('----------------------------------------------------------------------------------------------------')
    print('Initial state: ' + str((init_state+1)) + ' | Number of iterations: ' + str(num_it))
    print('Limit Distribution: ')
    print(next_dist)
    print('----------------------------------------------------------------------------------------------------')


if __name__ == '__main__':
    P = numpy.array([
        [1./3, 0., 2./3, 0., 0.],
        [1./4, 1./2, 1./4, 0., 0.],
        [1./2, 0., 1./2, 0., 0.],
        [0., 0., 0., 0., 1.],
        [0., 0., 0.,  2./3,  1./3]
    ])

    f = open('markov1.txt', 'w')

    sys.stdout = f

    for i in range(5):
        markov_simulate(init_state=i, stochastic_matrix=P, num_it=1000000)
