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