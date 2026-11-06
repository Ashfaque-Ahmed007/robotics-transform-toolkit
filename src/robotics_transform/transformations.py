import numpy as np

def make_transform(R, t):
    n = R.shape[0]
    T = np.zeros((n+1,n+1))
    T[0:n,0:n] = R
    T[:n,n] = t
    T[n,n] = 1

    return T

def inverse_transform(T):
    n = T.shape[0] - 1
    R = T[0:n,0:n]
    t = T[:n,n]
    R_inverse = R.T
    t_inverse = -R.T@t
    inverse_mat = np.zeros((n+1,n+1))
    inverse_mat[0:n,0:n] = R_inverse
    inverse_mat[:n,n] = t_inverse
    inverse_mat[n, n] = 1

    return inverse_mat

def compose_transform(T1, T2):
    """T1 is the first transformation you want to apply"""
    return T2 @ T1

def transform_point(T, p):
    n = p.shape[0]
    p_tilde = np.ones(n+1)
    p_tilde[:n] = p
    p_prime = T @ p_tilde
    return p_prime[:n]


