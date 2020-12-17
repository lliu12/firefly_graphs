import numpy as np

class Agent(object):
    def __init__(self, phase_length, jump, coords, pos = 0, delay = 0, inc = 1):
        self.phase_length = phase_length # how many steps until natural_firing (if no jumps used)
        self.jump = jump # a function that takes in positions of receiving and sending agents
        self.pos = pos # starting position from 0 to phase_length - 1
        self.delay = delay
        self.inc = inc # number of steps to increase pos by naturally at each simulation step

        self.neighbors = []
        self.coords = coords
        self.natural_firing = self.pos >= self.phase_length

    def reset(self):
        self.pos = 0
        self.natural_firing = False

    def phase_jump(self):
        j = self.jump(self.pos)
        self.pos += j
        if self.pos >= self.phase_length or self.pos <= 0:
            self.pos = self.phase_length
        # if self.pos >= self.phase_length: # remove this and nothing converges... interesting
        #     self.natural_firing = True

    # increment phase by 1
    def increment(self):
        self.pos += self.inc
        if self.pos >= self.phase_length or self.pos <= 0:
            self.natural_firing = True
            self.pos = self.phase_length

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def firing_neighbor(self):
        has_firing_neighbor = False
        for n in self.neighbors:
            if n.natural_firing:
                has_firing_neighbor = True
        return has_firing_neighbor


    