import numpy as np

class Agent(object):
    def __init__(self, phase_length, jump, coords, pos = 0, delay = 0, inc = 1):
        self.phase_length = phase_length # how many steps until firing (if no jumps used)
        self.jump = jump # how many steps to increase pos by if a neighbor fires
        self.pos = pos # starting position from 0 to phase_length - 1
        self.delay = delay
        self.inc = inc # number of steps to increase pos by naturally at each simulation step

        self.neighbors = []
        self.coords = coords
        self.firing = False

    def reset(self):
        self.pos = 0

    def phase_jump(self):
        self.pos += self.jump

    # increment phase by 1
    def increment(self):
        self.pos += self.inc

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def firing_neighbor(self):
        has_firing_neighbor = False
        for n in self.neighbors:
            if n.pos >= n.phase_length:
                has_firing_neighbor = True
        return has_firing_neighbor


    