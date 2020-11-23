import numpy as np
from agent import Agent
from event_handler import EventHandler

# mirollo paper: no chain reactions

class Simulation(object):
    def __init__(self, graph, graph_vertices, phase_length, jump, initial_positions, delay = 0, inc = 1):
        self.graph = graph
        self.graph_vertices = graph_vertices
        self.phase_length = phase_length
        self.jump = jump
        self.inc = inc
        self.steps_elapsed = 0
        self.steps_to_converge = None
        self.agents = [Agent(phase_length, jump, graph_vertices[i], pos = initial_positions[i], delay = delay, inc = inc) for i in range(len(graph))]
        for i, a in enumerate(self.agents):
            for j in range(len(self.graph[i])):
                if self.graph[i][j] == 1:
                    a.add_neighbor(self.agents[j])

        self.handler = EventHandler(self)

    def step(self):
        self.steps_elapsed += 1
        for a in self.agents: 
            assert a.pos < a.phase_length, "agent position greater than phase length at start of step"
            a.increment()
        for a in self.agents:
            if a.firing_neighbor() and a.pos >= a.delay:
                a.phase_jump()
        conv = True
        # if all agents are currently firing, system has converged
        for a in self.agents:
            if a.pos >= a.phase_length:
                # reset firing agents
                a.pos = 0
            else:
                conv = False
        if conv:
            self.steps_to_converge = self.steps_elapsed 

    # should this go back to initial positions (maybe make that one i) or regenerate random ? (random could be r)
    def reset(self):
        for i, a in enumerate(self.agents):
            a.pos = initial_positions[i]
