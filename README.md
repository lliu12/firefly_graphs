## Pulse-Coupled Oscillator Agents on Various Communication Graphs
### Developed for CS229r: Spectral Graph Theory Final Project

Pulse-coupled oscillators are nonlinear agents that maintain a phase, fire pulses, and respond to neighbors' pulses by changing their own phase. They have been 
used to model synchronizing fireflies, pacemaker cells, neurons, and more, and they are useful in developing network systems. We are interested in PCO systems 
that eventually synchronize, meaning all agents fire in unison. This code simulates systems with different dynamics on various communication graph structures 
(which determine which agents respond to each other), so we can study how graph structure and graph connectivity affects the behavior of a PCO system.

Use collect_data.py to produce a dataset with information on convergence probability, convergence time, and graph connectivity (via 2nd eigenvalue of Laplacian).
Use run_simulation.py to produce an animated visualization of a randomly generated system progressing. Below are screenshots of the visualization for a clique 
cycle graph (left) and a prime cycle with inverse chords (right). At this timestep, black nodes are not firing, yellow nodes fired naturally, and orange nodes 
are firing because responding to a yellow neighbor's firing brought them to firing as well.

<img src = "https://github.com/lliu12/firefly_graphs/blob/main/cc_simulation_screenshot.png?raw=true" width="400" height="400" /> <img src = "https://github.com/lliu12/firefly_graphs/blob/main/invchord_simulation_screenshot.png?raw=true" width="400" height="400" />
