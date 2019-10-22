import numpy
from matplotlib import pyplot


class PoissonProcess:
    def __init__(self, total_time, rate, init_state):
        self.total_time = total_time
        self.rate = rate
        self.count = [init_state]
        self.trans_time = [0.]
        self.step = 0

    def run(self):
        interval = numpy.random.exponential(scale=1./self.rate)
        while self.trans_time[self.step] + interval < self.total_time:
            self.trans_time.append(self.trans_time[self.step] + interval)
            self.count.append(self.count[self.step] + 1)
            self.step = self.step + 1
            interval = numpy.random.exponential(scale=1. / self.rate)
        self.trans_time.append(5.)
        self.count.append(self.count[self.step])

    def retrieve_data(self):
        return self.count, self.trans_time

    def reset(self, init_state):
        self.step = 0
        self.count, self.trans_time = [init_state], [0.]

    def integral(self):
        i = 0
        for j, time in enumerate(self.trans_time):
            if j != 0:
                i = i + (self.trans_time[j] - self.trans_time[j-1]) * self.count[j-1]
        return i


if __name__ == '__main__':
    J = 1

    poisson = PoissonProcess(total_time=5., rate=1., init_state=0)
    sigma = 0.

    for _ in range(J):
        poisson.run()
        n, t = poisson.retrieve_data()
        sigma = sigma + poisson.integral()
        pyplot.step(t, n, where='post')
        poisson.reset(init_state=0)

    pyplot.show()
