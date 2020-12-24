# collect data on convergence percentage and speed for systems and communication graphs

import sys, random, datetime, os, statistics, math
from agent import Agent
import graphs
from simulation import Simulation
import pygame
from pygame.locals import *
from pygame.color import *
import numpy as np
import pandas as pd 

rows_list = []
trials = 100 # trials per graph
phase_length = 10 # discretization of time
def jump(x): # choose PRC
    return x

delays = [0,5] # delay dynamics to test
for delay in delays:
    # this code uses random graph
    for i in range(1, 11):
        n = 30
        percent = i * 10

        print("Testing graphs of n = " + str(i))

        for _ in range(trials):
            graph = graphs.generate_rand(n, percent)
            vertices = np.around(graphs.rand_vertices(n,0,0)).astype(int)
            eig2 = graphs.lambda2(graph)
            params = {
            'graph': "random",
            'n': n,
            'percent': percent,
            # 'points_per_clique': n,
            'prc': "x", # x or optimal
            'phase_length': phase_length,
            'delay': delay,
            'initial_positions': "random", # random or constrained
            'lambda2': eig2
            }

            initial_positions = np.random.randint(0, phase_length, len(graph))
            # initial_positions = [i for i in np.random.randint(0, phase_length, c) for _ in range(n)] # for synced clique cycle
            sim = Simulation(graph, vertices, phase_length, jump, initial_positions = initial_positions, delay = delay)
            running = True

            while running:
                sim.step() 
                # terminate simulation if needed after 10000 steps
                if sim.steps_to_converge is not None or sim.steps_to_repeat is not None or sim.steps_elapsed > 10000:
                    running = False
                
            row = params.copy()
            row['converged'] = 0 if sim.steps_to_converge is None else 1
            row["steps_to_converge"] = sim.steps_to_converge if sim.steps_to_converge is not None else None
            row['repeated'] = 0 if sim.steps_to_repeat is None else 1
            row['steps_to_repeat'] = sim.steps_to_repeat if sim.steps_to_repeat is not None else None

            rows_list.append(row)

            
# save data
df = pd.DataFrame(rows_list)
df.to_csv("simulation_output.csv", index = False)

