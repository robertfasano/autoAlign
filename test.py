from parametric import Instrument
from optimistic.algorithms import GridSearch
import numpy as np
import time

class TestInstrument(Instrument):
    def __init__(self):
        super().__init__()
        self.add_parameter('x', 0, get_cmd=self.get_cmd, set_cmd=self.set_cmd)

    def set_cmd(self, value):
        print('SET', value)

    def get_cmd(self):
        print('GET', self.x.value)
        return self.x.value

    def optimize(self):
        print('Running optimization')
        t0 = time.time()
        grid = GridSearch(self.cost)
        grid.add_parameter(self.x, bounds=(-10, 10))
        grid.run()
        ms = (time.time() - t0) * 1000
        print('Optimization complete in %.0f ms'%ms)

        return ms

    def cost(self):
        return -np.exp(-(self.x-3)**2)

if __name__ == '__main__':
    inst = TestInstrument()
    inst.host('192.168.0.104:1105')
