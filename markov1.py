import sys
import numpy

N = 10000


class MarkovChain:
    def __init__(self, trans_prob):
        self.prob = trans_prob
        self.states = list(trans_prob.keys())
        self.freq = {s: 0 for s in self.states}
        self.num_iter = None

    def step_forward(self, curr_state):
        return numpy.random.choice(self.states, p=[self.prob[curr_state][next_state] for next_state in self.states])

    def distribution(self):
        if self.num_iter is not None:
            return [(s, float(self.freq[s] / self.num_iter)) for s in self.freq]
        return 'You must first simulate the chain. Use <markov>.run()'

    def run(self, init_state, num_iter):
        self.num_iter = num_iter
        for _ in range(num_iter):
            next_state = self.step_forward(curr_state=init_state)
            self.freq[next_state] = self.freq[next_state] + 1
            init_state = next_state

    def reset(self):
        self.num_iter = None
        self.freq = {s: 0 for s in self.states}


def output_results(s, m):
    print('----------------------------------------------------------------------------------------------------')
    print('Initial state: ' + s)
    print('Limit Distribution: ')
    print(m.distribution())
    print('----------------------------------------------------------------------------------------------------')


if __name__ == '__main__':
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
