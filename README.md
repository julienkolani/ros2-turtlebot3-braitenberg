# ROS2 TurtleBot3 Braitenberg

A ROS2 Python package implementing Braitenberg vehicle behaviors on TurtleBot3. Demonstrates reactive robot control where motor outputs are directly coupled to sensor inputs, producing emergent behaviors without explicit planning.

## Overview

Braitenberg vehicles exhibit complex-seeming behaviors (attraction, repulsion, fear, aggression) through simple sensor-motor coupling. This package applies the concept to TurtleBot3 using ROS2 sensor topics.

## Tech Stack

- Python
- ROS2 (Humble or later)
- TurtleBot3

## Setup

```bash
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
ros2 run py_turtlebot_braitenberg simple_braitenberg
```
