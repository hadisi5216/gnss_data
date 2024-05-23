### GNSS ROS2

> 数据格式
> 
> $GPFPD, GPSWeek, GPSTime, Heading, Pitch, Roll, Lattitude, Longitude, Altitude, Ve , Vn, Vu, Baseline, NSV1, NSV2, Status *cs<CR><LF>

* pyserial
```
pip3 install pyserial
```
* topic：
```
/sensing/gnss/gnss_data/nav_sat_fix
```
* launch
```
ros2 launch gnss_data gnss_data.launch.py 
```
