
import numpy as np

from robotics_transform import (
    axis_angle_to_quaternion,
    quaternion_to_rotation_matrix,
    euler_to_quaternion,
    quaternion_to_euler,
    quaternion_conjugate,
    quaternion_inverse,
)


def test_axis_angle_to_quaternion():
    q = axis_angle_to_quaternion(
        np.array([0, 0, 1]),
        np.pi / 2
    )

    expected = np.array([
        np.cos(np.pi / 4),
        0,
        0,
        np.sin(np.pi / 4)
    ])

    assert np.allclose(q, expected)


def test_quaternion_rotation_matrix():
    q = axis_angle_to_quaternion(
        np.array([0, 0, 1]),
        np.pi / 2
    )

    R = quaternion_to_rotation_matrix(q)

    assert np.allclose(R, [
        [0, -1, 0],
        [1,  0, 0],
        [0,  0, 1]
    ], atol=1e-7)


def test_euler_quaternion_conversion():
    angles = (0.3, 0.5, 0.8)

    q = euler_to_quaternion(*angles)
    recovered = quaternion_to_euler(q)

    assert np.allclose(recovered, angles)


def test_quaternion_inverse():
    q = euler_to_quaternion(0.3, 0.5, 0.8)
    q_inv = quaternion_inverse(q)

    assert np.allclose(q_inv, quaternion_conjugate(q))
    assert np.allclose(q_inv / np.linalg.norm(q_inv), 
                       quaternion_conjugate(q))


def test_quaternion_identity():
    q = euler_to_quaternion(0, 0, 0)

    assert np.allclose(q, [1, 0, 0, 0])