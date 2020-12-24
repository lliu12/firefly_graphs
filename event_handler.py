# handle user events

import sys, random, datetime, os, statistics, math
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk.pygame_util

class EventHandler(object):
    def __init__(self, simulation):
        self.sim = simulation
        self.running = True

    def handle_event(self, event):
        # press quit button in window corner to quit
        if event.type == QUIT:
            self.running = False

        # press R to reset
        elif event.type == KEYDOWN and event.key == K_r:
            self.sim.reset()

        # press P to print state history
        elif event.type == KEYDOWN and event.key == K_p:
            print("State History")
            for i in range(len(self.sim.history_list)):
                print(self.sim.history_list[i])
                if i == self.sim.steps_to_repeat:
                    print("Repeat Detected")
                if i == self.sim.steps_to_converge:
                    print("Convergence Detected")
            print("\n")