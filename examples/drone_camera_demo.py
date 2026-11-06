import numpy as np
import matplotlib.pyplot as plt

from robotics_transform import (euler_to_rotation_matrix, make_transform, compose_transform, transform_point)


# 1. Drone pose in the world frame

drone_position = np.array([3.0, 2.0, 5.0])

drone_orientation = euler_to_rotation_matrix(roll=0.0, pitch=0.0, yaw= np.pi / 2)

T_WD = make_transform(drone_orientation, drone_position)


# 2. Camera pose relative to the drone

camera_position = np.array([1.0, 0.0, 0.0])
camera_orientation = np.eye(3)

T_DC = make_transform(camera_orientation, camera_position)


# 3. Object position in the camera frame

object_camera = np.array([2.0, 1.0, 3.0])


# 4. Transform camera coordinates into world coordinates

T_WC = compose_transform(T_DC, T_WD)

object_world = transform_point(T_WC, object_camera)


print("Drone position in world:", drone_position)
print("Camera position in drone frame:", camera_position)
print("Object position in camera frame:", object_camera)

print("\nTransformation: Camera -> World")
print(T_WC)

print("\nObject position in world frame:", object_world)

assert np.allclose(object_world, [2.0, 5.0, 8.0])

print("\nSimulation successful!")


def draw_frame(ax, T, label, length=0.7):
    """
    Draw a coordinate frame using its homogeneous transformation.
    """
    origin = T[:3, 3]
    R = T[:3, :3]

    colors = ["red", "green", "blue"]
    labels = ["X", "Y", "Z"]

    for i in range(3):
        direction = R[:, i]

        ax.quiver(
            *origin,
            *direction,
            length=length,
            color=colors[i],
            normalize=True
        )

        endpoint = origin + direction * length
        ax.text(*endpoint, labels[i], color=colors[i])

    ax.text(*origin, label, fontsize=10, fontweight="bold")


# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Draw coordinate frames
draw_frame(ax, np.eye(4), "World", length=1.2)
draw_frame(ax, T_WD, "Drone")
draw_frame(ax, T_WC, "Camera")

# Plot drone and camera positions
ax.scatter(*drone_position, color="orange", s=80, label="Drone")
ax.scatter(*T_WC[:3, 3], color="purple", s=80, label="Camera")

# Plot observed object
ax.scatter(
    *object_world,
    color="black",
    marker="*",
    s=180,
    label="Object"
)

# Connect camera to observed object
camera_world = T_WC[:3, 3]

ax.plot(
    [camera_world[0], object_world[0]],
    [camera_world[1], object_world[1]],
    [camera_world[2], object_world[2]],
    linestyle="--",
    color="gray",
    label="Camera observation"
)


def draw_drone_body(ax, T_WD):
    # Drone body geometry in its local frame
    center = np.array([0, 0, 0])

    arms = [
        np.array([0.4, 0, 0]),
        np.array([-0.4, 0, 0]),
        np.array([0, 0.4, 0]),
        np.array([0, -0.4, 0]),
    ]

    def to_world(point):
        return transform_point(T_WD, point)

    world_center = to_world(center)

    for arm in arms:
        endpoint = to_world(arm)

        ax.plot(
            [world_center[0], endpoint[0]],
            [world_center[1], endpoint[1]],
            [world_center[2], endpoint[2]],
            color="orange",
            linewidth=3
        )

        ax.scatter(*endpoint, color="red", s=35)

    ax.scatter(*world_center, color="orange", s=100)


def draw_camera_frustum(ax, T_WC):
    # Camera looks along its local +Z axis
    z = 1.0
    half_width = 0.4
    half_height = 0.3

    corners_camera = [
        np.array([-half_width, -half_height, z]),
        np.array([ half_width, -half_height, z]),
        np.array([ half_width,  half_height, z]),
        np.array([-half_width,  half_height, z]),
    ]

    origin = T_WC[:3, 3]

    corners_world = [
        transform_point(T_WC, corner)
        for corner in corners_camera
    ]

    # Draw rays from camera to frustum corners
    for corner in corners_world:
        ax.plot(
            [origin[0], corner[0]],
            [origin[1], corner[1]],
            [origin[2], corner[2]],
            color="purple",
            alpha=0.6
        )

    # Draw the frustum rectangle
    for i in range(4):
        p1 = corners_world[i]
        p2 = corners_world[(i + 1) % 4]

        ax.plot(
            [p1[0], p2[0]],
            [p1[1], p2[1]],
            [p1[2], p2[2]],
            color="purple"
        )


draw_drone_body(ax, T_WD)
draw_camera_frustum(ax, T_WC)
ax.set_xlabel("World X (m)")
ax.set_ylabel("World Y (m)")
ax.set_zlabel("World Z (m)")
ax.set_title("Drone-Camera-Object Coordinate Transformation")

ax.legend()
ax.set_box_aspect([1, 1, 1])

plt.tight_layout()
plt.show()
