import numpy


class PoissonProcess:
    def __init__(self, total_time, rate, init_state):
        self.total_time = total_time
        self.rate = rate
        self.count = [init_state]
        self.trans_time = [0.]
        self.step = 0

    def simulate_uniform(self):
        total_arr = int(self.rate * self.total_time)
        self.trans_time = [numpy.random.uniform(0., self.total_time) for _ in range(total_arr)]
        self.trans_time.append(0.)
        self.trans_time.append(self.total_time)
        self.trans_time = sorted(self.trans_time)
        self.count = [i for i in range(total_arr + 2)]
        self.count[len(self.count) - 1] = self.count[len(self.count) - 2]

    def simulate_exponential(self):
        interval = numpy.random.exponential(scale=1./self.rate)
        while self.trans_time[self.step] + interval < self.total_time:
            self.trans_time.append(self.trans_time[self.step] + interval)
            self.count.append(self.count[self.step] + 1)
            self.step = self.step + 1
            interval = numpy.random.exponential(scale=1./self.rate)
        self.trans_time.append(self.total_time)
        self.count.append(self.count[self.step])

    def retrieve_data(self):
        return self.trans_time, self.count

    def reset(self, init_state):
        self.step = 0
        self.count, self.trans_time = [init_state], [0.]

    def integral(self):
        i = 0
        for j, time in enumerate(self.trans_time):
            if j != 0:
                i = i + (self.trans_time[j] - self.trans_time[j-1]) * self.count[j-1]
        return i
