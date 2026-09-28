"""Compute the UR5 hand position for many sets of joint angles.

Reads joint_angles.csv (one row = six angles in radians)
and writes positions.csv (x, y, z of the hand in metres).
"""
import csv
import numpy as np
import modern_robotics as mr

# UR5 dimensions in metres
W1, W2, L1, L2, H1, H2 = 0.109, 0.082, 0.425, 0.392, 0.089, 0.095

M = np.array([[-1, 0, 0, L1 + L2],
              [ 0, 0, 1, W1 + W2],
              [ 0, 1, 0, H1 - H2],
              [ 0, 0, 0, 1]])

Slist = np.array([[0, 0,  1,  0,       0,       0],
                  [0, 1,  0, -H1,      0,       0],
                  [0, 1,  0, -H1,      0,       L1],
                  [0, 1,  0, -H1,      0,       L1 + L2],
                  [0, 0, -1, -W1,      L1 + L2, 0],
                  [0, 1,  0,  H2 - H1, 0,       L1 + L2]]).T


def read_angles(path):
    """Return a list of joint-angle lists from a CSV file."""
    rows = []
    with open(path) as f:
        for line in csv.reader(f):
            rows.append([float(value) for value in line])
    return rows


def hand_position(thetas):
    """Return the (x, y, z) position of the hand for six joint angles."""
    T = mr.FKinSpace(M, Slist, thetas)
    return [round(float(v), 3) for v in T[:3, 3]]


def main():
    all_angles = read_angles("joint_angles.csv")
    with open("positions.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y", "z"])
        for thetas in all_angles:
            writer.writerow(hand_position(thetas))
    print(f"Wrote {len(all_angles)} positions to positions.csv")


if __name__ == "__main__":
    main()
