import numpy as np

def pagerank(M, num_iterations: int = 100, d: float = 0.85):

    N = M.shape[1]
    v = np.ones(N) / N
    M_hat = (d * M + (1 - d) / N)
    for i in range(num_iterations):
        v = M_hat @ v
    return v