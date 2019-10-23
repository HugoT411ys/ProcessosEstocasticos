import numpy


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
        s = 0
        for _ in range(num_iter):
            next_state = self.step_forward(curr_state=init_state)
            self.freq[next_state] = self.freq[next_state] + 1
            s = s + int(next_state)*int(next_state)
            init_state = next_state
        return float(s / num_iter)

    def reset(self):
        self.num_iter = None
        self.freq = {s: 0 for s in self.states}