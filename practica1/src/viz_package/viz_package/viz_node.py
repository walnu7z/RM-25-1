import rclpy 
from rclpy.node import Node
from visualization_msgs.msg import Marker
import serial
import random
import re
import time

serial_port = '/dev/ttyACM0';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
ser = serial.Serial(serial_port, baud_rate)

class MarkerPublisher(Node):
    def __init__(self):
        self.count = 0
        super().__init__('marker_publisher')
        self.publisher_ = self.create_publisher(Marker, 'marker_topic', 10)
        timer_period = 0.002 # seconds 
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self): 
        marker = Marker()
        marker.header.frame_id = "/base_link" 
        marker.header.stamp = self.get_clock().now().to_msg()

        x_coord = getDist()
    # set shape, Arrow: 0; Cube: 1  Sphere: 2 Cylinder: 3
        marker.type = 1 
        marker.id = self.count
        marker.scale.x = 7.0
        marker.scale.y = 7.0
        marker.scale.z = 7.0
        marker.color.r = 0.0
        marker.color.g =  1.0
        marker.color.b = 0.0
        marker.color.a = 0.5
        marker.lifetime.sec = 10
        marker.pose.position.x =  x_coord
        marker.pose.position.y =  0.0
        marker.pose.position.z = 0.0
        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0  
        marker.pose.orientation.z = 0.0 
        marker.pose.orientation.w = 1.0 
        self.count += 1
        self.publisher_.publish(marker)

def main(arg=None):
    print('HI from viz_package')
    rclpy.init(args=arg)
    marker_publisher = MarkerPublisher()
    rclpy.spin(marker_publisher)
    ser.close()
    marker_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

#Lee y calcula el promedio de lecturas del sensor especificado por num_captures
def getDist():
    num_captures = 3 
    dist = []
    while num_captures > 0:
        try:
            line = ser.readline();
            line = line.decode("utf-8", "strict") #ser.readline returns a binary, convert to string
            #line = extract_last_number(line)
            #print(dist, ' average: ', )
            num = float(line)
            dist.append(num)
            #for debugging purposes
            #dist.append(random.randint(0, 100)/1)
            num_captures -= 1
        except:
            pass
    #print(dist, ' average: ', sum(dist)/len(dist))
    return sum(dist)/len(dist)

# Return the last numeric value if found, else return None
def extract_last_number(s):
    # Find all numeric values in the string
    numbers = re.findall(r'\d+', s)
    return int(numbers[-1]) if numbers else None
