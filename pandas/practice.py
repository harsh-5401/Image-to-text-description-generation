import numpy as np

def create_2d_matrix(n,m):
    matrix = np.random.randint(0,2, (n, m))
    return matrix

def create_3d_matrix(n,m,p):
    matrix = np.random.randint(0,2, (n,m,p))
    return matrix

matrx = create_2d_matrix(6,4)


print(matrx)