import numpy as np

# argggg ok i am going to need to make paired up draw_graph functions too.. 
# so maybe the class structure actually will be necessary to keep that from getting gross
# i guess each graph can just be its own class and all graph's classes will have same function names LOL
# graph.coords fn to get coordinates of each vertex in drawing

def generate_complete(n):
    return np.ones((n, n), dtype = int)

# num vertices, screen width, screen height
def complete_vertices(n, w, h):
    center = np.array([w / 2, h / 2])
    rad = .8 * min(w, h) / 2
    points = [rad * np.array([np.cos(i * 2 * np.pi / n), np.sin(i * 2 * np.pi / n)]) + center for i in range(n)]
    return points


def generate_cycle(n):
    g = np.zeros((n,n), dtype = int)
    for i in range(n):
        g[i][(i + 1) % n] = 1
        g[(i + 1) % n][i] = 1
    return g

def generate_path(n):
    g = np.zeros((n,n), dtype = int)
    for i in range(n - 1):
        g[i][(i + 1) % n] = 1
        g[(i + 1) % n][i] = 1
    return g


# would be cool to gen. more bipartite or periodic graphs

# lattice graph with connected neighbors

def generate_grid(r,c, activation_dist = 1):
    g = np.zeros((r * c, r * c))
    for i in range(r * c):
        for j in range(r * c):
            y1 = i % c
            x1 = i // c
            y2 = j % c
            x2 = j // c
            if np.abs(x1 - x2) + np.abs(y1 - y2) <= activation_dist:
                g[i][j] = 1
    return g


    # trees
    # complete bipartite graph
    # cube - two vertices adj if they differ in a single position