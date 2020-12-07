# handle user events

import sys, random, datetime, os, statistics, math
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk.pygame_util

# have simulation file call this
class EventHandler(object):
    def __init__(self, simulation):
        self.sim = simulation
        self.running = True

    def handle_event(self, event):
        if event.type == QUIT:
            self.running = False

        elif event.type == KEYDOWN and event.key == K_r:
            self.sim.reset()

        elif event.type == KEYDOWN and event.key == K_p:
            print("State History")
            for i in range(len(self.sim.state_history)):
                print(self.sim.state_history[i])
                if i == self.sim.steps_to_repeat:
                    print("Repeat Detected")
                if i == self.sim.steps_to_converge:
                    print("Convergence Detected")
            print("\n")