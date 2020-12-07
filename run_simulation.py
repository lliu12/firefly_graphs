
import sys, random, datetime, os, statistics, math
from agent import Agent
import graphs
from simulation import Simulation
import pygame
from pygame.locals import *
from pygame.color import *
import numpy as np

DISPLAY_SIZE = (500,500)
w,h = DISPLAY_SIZE

## code for using cycle graph
n = 13
# graph = graphs.generate_pchord(n)
# vertices = np.around(graphs.pchord_vertices(n, w, h)).astype(int)

graph = graphs.generate_complete(n)
vertices = np.around(graphs.complete_vertices(n, w, h)).astype(int)

# # code for using grid graph
# r = 5
# c = 5
# graph = graphs.generate_grid(r, c)
# vertices = graphs.grid_vertices(r,c, w,h)


phase_length = 10
# def jump(x):
#     return x

# def jump(x, phase_length = phase_length):
#     val = -x if x <= phase_length / 2 else phase_length - x
#     return val
def jump(x, phase_length = phase_length):
    l = 1
    if x <= phase_length:
        return -x * l
    else: 
        return (phase_length - x) * l
    

delay = 5
initial_positions = np.random.randint(0, phase_length, len(graph))

# run game
def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY_SIZE, 0) 
    _, height = screen.get_size()
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 16)

    sim = Simulation(graph, vertices, phase_length, jump, initial_positions = initial_positions, delay = delay)

    while running:
        for event in pygame.event.get():
            # returns false if the event is one that tells the simulation to quit
            sim.handler.handle_event(event)
            running = sim.handler.running

        # Update physics
        fps = 2
        
        jumped = sim.step() # any way to be able to visualize what things jumped?


        screen.fill(THECOLORS["white"])
        for a in sim.agents:
            for n in a.neighbors:
                pygame.draw.aaline(screen, THECOLORS["lightskyblue1"], a.coords, n.coords)
        for a in sim.agents:
            screen.blit(font.render(str(a.pos), 1, THECOLORS["darkgrey"]), (a.coords[0], a.coords[1] + 10))
            if a.pos == 0 or a.pos >= a.phase_length:
                if a not in jumped:
                    pygame.draw.circle(screen, THECOLORS["yellow"], a.coords, 5)
                else: 
                    pygame.draw.circle(screen, THECOLORS["orange"], a.coords, 5)
            else: 
                pygame.draw.circle(screen, THECOLORS["black"], a.coords, 5)
                
        screen.blit(font.render("steps elapsed: " + str(sim.steps_elapsed), 1, THECOLORS["darkgrey"]), (5,5))
        if sim.steps_to_converge is not None:
            screen.blit(font.render("steps to converge: " + str(sim.steps_to_converge), 1, THECOLORS["darkgrey"]), (5,15))
        if sim.steps_to_repeat is not None:
            screen.blit(font.render("steps to repeat: " + str(sim.steps_to_repeat), 1, THECOLORS["darkgrey"]), (5,25))

        pygame.display.flip()
        clock.tick(fps)
        
if __name__ == '__main__':
    sys.exit(main())