import numpy as np

def rotation_x(theta):
    R = np.array([
        [1, 0,             0            ],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])
    return R

def rotation_y(theta):
    R = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [ 0,             1, 0            ],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return R

def rotation_z(theta):
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])
    return R

def inverse_rotation(R):
    return R.T

def euler_to_rotation_matrix(roll, pitch, yaw):
    Rx = rotation_x(roll)
    Ry = rotation_y(pitch)
    Rz = rotation_z(yaw)
    return Rz @ Ry @ Rx

def rotation_matrix_to_euler(R):
    pitch = np.arcsin(-R[2,0])
    roll = np.arctan2(R[2,1],R[2,2])
    yaw = np.arctan2(R[1,0],R[0,0])

    return (roll,pitch, yaw)

