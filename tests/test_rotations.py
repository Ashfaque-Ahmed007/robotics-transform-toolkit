
import numpy as np

from robotics_transform import (
    rotation_x,
    rotation_y,
    rotation_z,
    euler_to_rotation_matrix,
    rotation_matrix_to_euler,
)


def test_rotation_matrix_properties():
    for R in [rotation_x(0.5), rotation_y(0.7), rotation_z(1.2)]:
        assert np.allclose(R.T @ R, np.eye(3))
        assert np.isclose(np.linalg.det(R), 1.0)


def test_rotation_x():
    R = rotation_x(np.pi / 2)
    p = R @ np.array([0, 1, 0])

    assert np.allclose(p, [0, 0, 1])


def test_rotation_y():
    R = rotation_y(np.pi / 2)
    p = R @ np.array([0, 0, 1])

    assert np.allclose(p, [1, 0, 0])


def test_rotation_z():
    R = rotation_z(np.pi / 2)
    p = R @ np.array([1, 0, 0])

    assert np.allclose(p, [0, 1, 0])


def test_euler_conversion():
    angles = (0.3, 0.5, 0.8)

    R = euler_to_rotation_matrix(*angles)
    recovered = rotation_matrix_to_euler(R)

    assert np.allclose(recovered, angles)
