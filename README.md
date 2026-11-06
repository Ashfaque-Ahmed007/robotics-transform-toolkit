# Robotics Transform Toolkit

A Python toolkit for 3D coordinate transformations in robotics, built using NumPy.

This project implements fundamental mathematical operations used in robotics, computer vision, and autonomous systems.

## Features

- 3D rotation matrices (X, Y, Z axes)
- Euler angle conversions (ZYX convention)
- Quaternion representations and conversions
- Quaternion conjugate and inverse
- Homogeneous transformation matrices
- Transformation composition and inversion
- 3D point transformations between coordinate frames
- Drone-camera-object simulation
- 3D visualization using Matplotlib

## Project Structure

```text
robotics-transform-toolkit/
├── src/
│   └── robotics_transform/
│       ├── __init__.py
│       ├── rotations.py
│       ├── quaternions.py
│       └── transformations.py
├── tests/
│   ├── test_rotations.py
│   ├── test_quaternions.py
│   └── test_transformations.py
├── examples/
│   └── drone_camera_demo.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Mathematical Conventions

- Right-handed coordinate systems.
- Column vectors.
- Angles are measured in radians.
- Distances are measured in metres.
- Quaternions use `(w, x, y, z)` ordering.
- Euler angles follow the ZYX convention:

$$R = R_z(\psi)R_y(\theta)R_x(\phi)$$

- Homogeneous transformations use 4 × 4 matrices.

A transformation \({}^{A}T_B\) converts coordinates expressed in frame B into coordinates expressed in frame A.

### Homogeneous Transformation

$$
T =
\begin{bmatrix}
R & t\\
0 & 1
\end{bmatrix}
$$

A point is transformed using:

$$
{}^Ap = {}^AT_B\,{}^Bp
$$

### Transformation Composition

$$
{}^AT_C = {}^AT_B\,{}^BT_C
$$

The rightmost transformation is applied first.

### Inverse Transformation

$$
T^{-1} =
\begin{bmatrix}
R^T & -R^Tt\\
0 & 1
\end{bmatrix}
$$

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd robotics-transform-toolkit
```

Install dependencies:

```bash
uv sync --all-groups
```

## Usage

```python
import numpy as np

from robotics_transform import (
    rotation_z,
    make_transform,
    transform_point,
)

R = rotation_z(np.pi / 2)
t = np.array([3.0, 2.0, 5.0])

T = make_transform(R, t)

point = np.array([1.0, 0.0, 0.0])

transformed_point = transform_point(T, point)

print(transformed_point)
```

## Drone-Camera Simulation

The example simulates a drone carrying a camera and observing an object.

The object's position in the world frame is calculated using:

$$
{}^Wp_O = {}^WT_D\,{}^DT_C\,{}^Cp_O
$$

Run the simulation:

```bash
uv run python examples/drone_camera_demo.py
```

The simulation includes:

- Drone pose in the world frame.
- Camera mounting transformation.
- Object position in camera coordinates.
- Object position in world coordinates.
- 3D coordinate-frame visualization.
- Simplified drone geometry and camera frustum.

## Testing

Run the unit tests:

```bash
uv run pytest -v
```

The test suite verifies rotation properties, quaternion conversions, transformation composition, inversion, and point transformations.

## Technologies

- Python
- NumPy
- Matplotlib
- Pytest
- uv

## Learning Objectives

This project was developed to build a practical understanding of 3D geometry and coordinate transformations used in robotics.

Future extensions could include camera calibration, projection models, rigid-body pose estimation, and integration with robotics simulation environments.
