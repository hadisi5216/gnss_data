#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import serial
import time

class NodePublisher(Node):
    def __init__(self,name):
        super().__init__(name)
        
        self.ser = serial.Serial('/dev/ttyUSB0', 115200)
        # 创建发布者
        self.gps_publisher = self.create_publisher(NavSatFix,"/sensing/gnss/gnss_data/nav_sat_fix",10)
    
        while True:
            data = self.ser.readline().decode('utf-8')
            self.get_logger().info(f'GPS data:[{data}]')
            dataList = data.split(",")
            latitude = float(dataList[6])
            longitude = float(dataList[7])
            altitude = float(dataList[8])
            service = int(dataList[13])
            msg = NavSatFix()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = "gnss_link"
            msg.status.service = service
            msg.latitude = latitude
            msg.longitude = longitude
            msg.altitude = altitude
            
            self.gps_publisher.publish(msg)


            

def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = NodePublisher("gnss_data_publisher")  # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy