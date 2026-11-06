
import numpy as np

from robotics_transform import (
    rotation_z,
    make_transform,
    inverse_transform,
    compose_transform,
    transform_point,
)


def test_make_transform():
    R = rotation_z(np.pi / 2)
    t = np.array([1, 2, 3])

    T = make_transform(R, t)

    assert T.shape == (4, 4)
    assert np.allclose(T[:3, :3], R)
    assert np.allclose(T[:3, 3], t)


def test_inverse_transform():
    T = make_transform(
        rotation_z(np.pi / 2),
        np.array([1, 2, 3])
    )

    T_inv = inverse_transform(T)

    assert np.allclose(T_inv @ T, np.eye(4))
    assert np.allclose(T @ T_inv, np.eye(4))


def test_compose_transform():
    T1 = make_transform(np.eye(3), np.array([1, 0, 0]))
    T2 = make_transform(np.eye(3), np.array([0, 2, 0]))

    T = compose_transform(T1, T2)

    assert np.allclose(T[:3, 3], [1, 2, 0])


def test_transform_point():
    T = make_transform(
        rotation_z(np.pi / 2),
        np.array([3, 2, 5])
    )

    p = np.array([1, 0, 0])
    result = transform_point(T, p)

    assert np.allclose(result, [3, 3, 5])
