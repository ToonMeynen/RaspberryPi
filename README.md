# RaspberryPi
Folder with all my examples, tests and other crap. 

# Automatic light switch without the need of a light sensor. 
This sensor logs every mesurement. And when the sun is down it will swith on a light for 20 seconds. It calculates sunrise 
and sunset with the ephem module. No ligt sensor is needed this way.

# Goals
- Make a dashboard with the sensor data. 
- After 20 seconds the light switches off. In some situations this is to short. 
Program logic to keep the light on as long as there is activity. 
