import numpy as np
from .rotations import rotation_matrix_to_euler

def axis_angle_to_quaternion(axis, theta):
    norm_axis = axis/np.linalg.norm(axis)
    w = np.cos(theta/2)
    x = norm_axis[0] * np.sin(theta/2)
    y = norm_axis[1] * np.sin(theta/2)
    z = norm_axis[2] * np.sin(theta/2)

    return np.array([w, x, y, z])

def quaternion_to_rotation_matrix(q):
    w, x, y, z = q

    R = np.array([
        [1 - 2*(y**2 + z**2), 2*(x*y - w*z),     2*(x*z + w*y)],
        [2*(x*y + w*z),      1 - 2*(x**2 + z**2), 2*(y*z - w*x)],
        [2*(x*z - w*y),      2*(y*z + w*x),      1 - 2*(x**2 + y**2)]
    ])

    return R

def euler_to_quaternion(roll, pitch, yaw):
    cr = np.cos(roll / 2)
    sr = np.sin(roll / 2)
    cp = np.cos(pitch / 2)
    sp = np.sin(pitch / 2)
    cy = np.cos(yaw / 2)
    sy = np.sin(yaw / 2)

    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return np.array([w, x, y, z])

def quaternion_to_euler(q):
    R = quaternion_to_rotation_matrix(q)
    return rotation_matrix_to_euler(R)

def quaternion_conjugate(q):
    w, x, y, z = q
    return np.array([w, -x, -y, -z])


def quaternion_inverse(q):
    return quaternion_conjugate(q) / np.dot(q, q)