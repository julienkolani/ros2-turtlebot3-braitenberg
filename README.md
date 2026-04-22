# ROS2 TurtleBot3 Braitenberg

Package ROS2 Python implémentant les véhicules de Braitenberg sur TurtleBot3.

## Présentation

Les véhicules de Braitenberg produisent des comportements complexes (attraction, répulsion, peur) par simple couplage direct capteurs → moteurs, sans planification explicite. Ce package applique ce principe au TurtleBot3 via les topics ROS2.

## Stack technique

- Python, ROS2, TurtleBot3

## Installation

```bash
source /opt/ros/humble/setup.bash
colcon build && source install/setup.bash
ros2 run py_turtlebot_braitenberg simple_braitenberg
```
