
import numpy as np

A = np.matrix( ((1,2,3), (2,7,4)) )
B = np.matrix( ((1, -1), (0, 1)) )
C = np.matrix( ((5, -1), (9, 1), (6, 0)) )
D = np.matrix( ((3, -2, -1), (1, 2, 3)) )
u = np.array( [6, 2, -3, 5] )
v = np.array( [3, 5, -1, 4] )
w = np.matrix( ((1), (8), (0), (5)) )

alpha = 6

uv = u + v
uv2 = u - v
alpha_u = alpha * u
uv_dot = np.dot(u, v)
u_norm = np.linalg.norm(u)


print(uv, uv2, alpha_u, uv_dot, u_norm)

