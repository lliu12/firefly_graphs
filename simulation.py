import numpy as np
from agent import Agent
from event_handler import EventHandler

# mirollo paper: no chain reactions

class Simulation(object):
    def __init__(self, graph, graph_vertices, phase_length, jump, initial_positions, delay = 0, inc = 1):
        self.graph = graph
        self.graph_vertices = graph_vertices
        self.phase_length = phase_length
        self.jump = jump # a function that takes in positions of receiving agent
        self.inc = inc
        self.steps_elapsed = 0
        self.steps_to_converge = None # steps for all agents to synchronize
        self.steps_to_repeat = None # steps for a cycle in the system state to be identified (so system will not converge)
        self.agents = [Agent(phase_length, jump, graph_vertices[i], pos = initial_positions[i], delay = delay, inc = inc) for i in range(len(graph))]
        for i, a in enumerate(self.agents):
            for j in range(len(self.graph[i])):
                if self.graph[i][j] == 1:
                    a.add_neighbor(self.agents[j])

        self.handler = EventHandler(self)
        self.state_history = [self.current_state()]

    # returns list of agents that jumped in response to a neighbor this step
    def step(self):
        jumped = []
        self.steps_elapsed += 1
        for a in self.agents: 
            assert a.pos < a.phase_length, "agent position greater than phase length at start of step"
            a.increment()
        for a in self.agents: # not accurate! can't distinguish between if neighbor already fired or not...
            if a.firing_neighbor() and a.pos >= a.delay and a.pos < a.phase_length:
                a.phase_jump()
                jumped.append(a)
        conv = True
        # if all agents are currently natural_firing, system has converged
        for a in self.agents:
            if a.natural_firing or a.pos >= a.phase_length or a.pos == 0:
                a.reset()
            else:
                conv = False
        if conv and self.steps_to_converge is None:
            self.steps_to_converge = self.steps_elapsed 

        cur = self.current_state()
        if self.steps_to_repeat is None and cur in self.state_history:
            self.steps_to_repeat = self.steps_elapsed
        self.state_history.append(cur)
        return jumped

    # should this go back to initial positions (maybe make that one i) or regenerate random ? (random could be r)
    def reset(self):
        initial_positions = np.random.randint(0, self.phase_length, len(self.graph))
        for i, a in enumerate(self.agents):
            a.pos = initial_positions[i]
        self.steps_elapsed = 0
        self.steps_to_converge = None
        self.steps_to_repeat = None

    def current_state(self):
        return [a.pos for a in self.agents]
