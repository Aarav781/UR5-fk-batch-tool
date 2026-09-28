# UR5 FK Batch Tool

A Python tool from my Programming for Everybody course (Michigan, via Coursera). 
It reads a list of UR5 joint angles from a CSV file and computes where the robot's 
hand ends up for each one, using forward kinematics from Modern Robotics.

## Files
- `joint_angles.csv` — input: one row per set of 6 joint angles (radians)
- `batch_fk.py` — reads the input, computes each hand position, writes the output
- `positions.csv` — output: x, y, z of the hand for each row

## Run it
## Checking it
The second row uses the same angles as my UR5 CoppeliaSim simulation. 
The script's output (0.48, 0.634, 0.308) matches the simulator's result.

## What I learned
- How to read and write CSV files in Python
- Turning one working example into a function that handles many inputs
- Checking my code's output against a simulator to catch mistakes
