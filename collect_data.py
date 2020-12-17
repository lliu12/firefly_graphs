# for every trial, want to collect:
# whether it converged or repeated
# what step the convergence or repitition was detected

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
trials = 100

phase_length = 10
def jump(x):
    return x

delay = 5

for i in range(1, 30):
    n = 10
    c = i
    # make graph
    # graph = graphs.generate_dumbbell(n)
    # vertices = np.around(graphs.dumbbell_vertices(n, 0, 0)).astype(int)
    graph = graphs.generate_clique_cycle(c, n)
    vertices = np.around(graphs.clique_cycle_vertices(c,n,0,0)).astype(int)
    eig2 = graphs.lambda2(graph)

    print("Testing graphs of n = " + str(i))

    params = {
    'graph': "dumbbell",
    'c': c,
    'n': n,
    'prc': "x", # x or optimal
    'phase_length': phase_length,
    'delay': delay,
    'initial_positions': "random", # random or constrained
    'lambda2': eig2
    }

    for _ in range(trials):
        initial_positions = np.random.randint(0, phase_length, len(graph))
        sim = Simulation(graph, vertices, phase_length, jump, initial_positions = initial_positions, delay = delay)
        running = True

        while running:
            sim.step() 
            if sim.steps_to_converge is not None or sim.steps_to_repeat is not None or sim.steps_elapsed > 10000:
                running = False
            
        row = params.copy()
        row['converged'] = 0 if sim.steps_to_converge is None else 1
        row["steps_to_converge"] = sim.steps_to_converge if sim.steps_to_converge is not None else None
        row['repeated'] = 0 if sim.steps_to_repeat is None else 1
        row['steps_to_repeat'] = sim.steps_to_repeat if sim.steps_to_repeat is not None else None

        rows_list.append(row)
        












df = pd.DataFrame(rows_list)
df.to_csv("clique_cycle_delay5.csv", index = False)




# run chosen simulation 100 times and add rows to graph!

# save dataframe to file

# done!!