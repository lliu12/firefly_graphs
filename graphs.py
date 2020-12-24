# functions for generating adj matrices of communication graphs

import numpy as np

# complete graph
def generate_complete(n):
    return np.ones((n, n), dtype = int)

# num vertices, screen width, screen height
def complete_vertices(n, w, h):
    center = np.array([w / 2, h / 2])
    rad = .8 * min(w, h) / 2
    points = [rad * np.array([np.cos(i * 2 * np.pi / n), np.sin(i * 2 * np.pi / n)]) + center for i in range(n)]
    return points

# cycle graph
def generate_cycle(n):
    g = np.zeros((n,n), dtype = int)
    for i in range(n):
        g[i][(i + 1) % n] = 1
        g[(i + 1) % n][i] = 1
    return g

def cycle_vertices(n, w, h):
    return complete_vertices(n,w,h)

# prime chord 3-regular graph
# best defined if p prime, but still not a true expander
def generate_pchord(n):
    g = np.zeros((n,n), dtype = int)
    for i in range(n):
        g[i][(i + 1) % n] = 1
        g[(i + 1) % n][i] = 1
        for j in range(n):
            if (i * j % n == 1):
                g[i][j] = 1
                g[j][i] = 1
    # also make -1, 1 an edge since they're both sq roots of 1
    g[1][-1] = 1
    g[-1][1] = 1
    return g

def pchord_vertices(n, w, h):
    return complete_vertices(n,w,h)

# path graph (cycle without ends connected)
def generate_path(n):
    g = np.zeros((n,n), dtype = int)
    for i in range(n - 1):
        g[i][(i + 1) % n] = 1
        g[(i + 1) % n][i] = 1
    return g

def path_vertices(n, w, h):
    return complete_vertices(n,w,h)

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

# rows, cols, screen width, screen height
def grid_vertices(rownum,colnum, w, h):
    cols = np.linspace(.1 * w, .9 * w, colnum)
    rows = np.linspace(.1 * h, .9 * h, rownum)
    points = [(r,c) for c in cols for r in rows]
    return points

# dumbbell graph
def generate_dumbbell(n): # where n is the number of verts in one "weight" of the dumbbell
    g = np.zeros((2 * n, 2 * n))
    for i in range(n):
        for j in range(n):
            g[i][j] = 1
            g[n + i][n + j] = 1
    g[0][-1] = 1
    g[-1][0] = 1
    return g

def dumbbell_vertices(n, w, h):
    p1 = complete_vertices(n, w/2, h)
    p2 = [np.array([w - i[0], i[1]]) for i in p1]
    return p1 + p2

# clique cycle graph
# c = number of cliques arranged in a cycle, n = number of nodes per clique
def generate_clique_cycle(c, n = 10):
    g = np.zeros((c * n, c * n))
    for i in range(n):
        for j in range(n):
            for cc in range(c):
                g[cc * n + i][cc * n + j] = 1
                
    # bridges between first and last clique
    g[0][-1] = 1
    g[-1][0] = 1
    
    # bridges for rest of cycle
    for cc in range(1, c):
        g[n * cc][n * cc - 1] = 1
        g[n * cc - 1][n * cc] = 1
    return g

def clique_cycle_vertices(c, n, w, h):
    cycle_center = np.array([w / 2, h / 2])
    rad = .8 * min(w, h) / 2
    clique_centers = [rad * np.array([np.cos(i * 2 * np.pi / c), np.sin(i * 2 * np.pi / c)]) + cycle_center for i in range(c)]
    clique_rad = rad * .2
    points = [clique_rad * np.array([np.cos(i * 2 * np.pi / n), np.sin(i * 2 * np.pi / n)]) + clique_centers[cc] for cc in range(c) for i in range(n)]
    return points

# graph with random percentage of edges included
def generate_rand(n, percent):
    # edges in complete simple graph
    all_edges = []
    for i in range(n):
        for j in range (i):
                all_edges.append([i,j])
    edges_to_get = int(np.ceil(percent * len(all_edges) / 100))
    edge_indices = np.random.choice(range(len(all_edges)), edges_to_get, replace = False)
    edges = np.array(all_edges)[edge_indices]
    
    g = np.zeros((n, n))
    for i,j in edges:
        g[i][j] = 1
        g[j][i] = 1
    return g

def rand_vertices(n, w, h):
    return complete_vertices(n,w,h)

# get second eigenvalue of laplacian, given A
def lambda2(A):
    degrees = np.sum(A, axis = -1)
    D = np.diag(degrees)
    L = D - A
    eigvals, eigvecs = np.linalg.eig(L)
    eigvals.sort()
    if len(eigvals) >= 2:
        if eigvals[1].imag > .001:
            print("nontrivial complex component to eval")
        return eigvals[1].real
    else:
        return 0

