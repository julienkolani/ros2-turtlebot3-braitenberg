import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class SimpleBraitenberg(Node):

    def __init__(self):
        super().__init__('simple_braitenberg')

        qos = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.BEST_EFFORT  
        )

        self.scan_subscriber = self.create_subscription(LaserScan, 'scan', self.scan_callback, qos)
        self.scan_subscriber  
        self.vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

    def scan_callback(self, scan):
        #TODO
        #TODO
        #TODO
        #TODO
        #TODO

		#Envoi de la commande en vitesse au tb
        vel_msg = Twist()
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.0
        self.vel_publisher.publish(vel_msg)


def main(args=None):
    rclpy.init(args=args)

    simple_braitenberg = SimpleBraitenberg()
    rclpy.spin(simple_braitenberg)

    simple_braitenberg.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
