import cv2
import numpy as np
from point import Point
from surface import Surface
from camera import Camera
import time
import matplotlib.pyplot as plt
from datetime import datetime
from pwmController import PWMController


x_axis = PWMController(18, 7.6)
y_axis = PWMController(19, 6.6)
camera = Camera()
surfaceMatrix = camera.readAsGrayScaleMatrix()
surface = Surface(surfaceMatrix)
print(surface)
print(surfaceMatrix)

plt.imshow(surfaceMatrix,cmap='gray',vmin=0,vmax=255)
plt.axis('off')
plt.show()

prevTime =  -1
currTime =  datetime.now().time()
prevBallLocation = -1
currBallLocation = -1
surfaceMatrix = camera.readAsGrayScaleMatrix()
pointInBall = surface.findPointInBall(surfaceMatrix)

'''
log_file_path = 'image.txt'
with open(log_file_path, 'w' ) as log_file:
    for row in surfaceMatrix:
        log_file.write(' '.join(map(str,row)) + '\n')
'''



#while(1) for findinf the first time that ball is on the surface:
while(1):
    surfaceMatrix = camera.readAsGrayScaleMatrix()
    pointInBall = surface.findPointInBall(surfaceMatrix)
    if(pointInBall.x == -1):
        print("No ball was found")
    else:
        currBallLocation = surface.findMiddleOfBall(pointInBall, surfaceMatrix)
        currTime =  time.time()
        print("Current time is:", currTime)
        break
   
prevBallLocation = currBallLocation
time1 =  time.time()
count = 0
x_target = 0
y_target = 0
maxAngle = 0.3
P_factor = 1
D_factor = 3
maxLength = 200
maxSpeed = 1000
time.sleep(1)


while(1):
    surfaceMatrix = camera.readAsGrayScaleMatrix()
    pointInBall = surface.findPointInBall(surfaceMatrix)
    if(pointInBall.x == -1):
        print("No ball was found")
    else:
        prevBallLocation = currBallLocation
        currBallLocation = surface.findMiddleOfBall(pointInBall, surfaceMatrix)
        print(currBallLocation)
        prevTime = currTime
        currTime =  time.time()
        deltaTime = currTime - prevTime
        delta_X = currBallLocation.x
        delta_Y = currBallLocation.y
        speed_X = (currBallLocation.x - prevBallLocation.x) /deltaTime
        speed_Y = (currBallLocation.y - prevBallLocation.y) /deltaTime
        angleY = maxAngle *(P_factor*(delta_X / maxLength) + D_factor*(speed_X/maxSpeed))
        angleX = maxAngle *(P_factor*(delta_Y / maxLength) + D_factor*(speed_Y/maxSpeed))
        x_axis.set_x_pwm(angleX)
        y_axis.set_y_pwm(angleY)
        time.sleep(0.05)

        
        



  




