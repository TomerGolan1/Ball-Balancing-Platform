import math
from point import Point

class Surface:
    def __init__(self, surfaceMatrix ):
        """
        Initialize a new point at the given coordinates.

        :param xBorder: The distance between middle of the matrix to the side border
        :param yBorder: The distance between middle of the matrix to upper/lower border
        """
        self.xCenter = int(len(surfaceMatrix[0])/2)
        self.yCenter = int(len(surfaceMatrix)/2)
        self.middleColor = surfaceMatrix[self.yCenter][self.xCenter] 
        print(f"y-middle {int(len(surfaceMatrix)/2)}")
        print(f"x middle  {int(len(surfaceMatrix[0])/2)} ")
        self.upperYborder = -1
        self.lowerYborder= -1
        self.delta = 15
        self.rightXborder = -1
        self.leftXborder= -1

        self.ballColor = -1
        for x in range(self.xCenter,1,-5):
            if(abs(int(surfaceMatrix[self.yCenter][x]) - int(self.middleColor)) > 40):
                self.leftXborder = x    
                print(x)        
                break
        for x in range(self.xCenter,len(surfaceMatrix[0])-2, 5):
            if(abs(int(surfaceMatrix[self.yCenter][x]) - int(self.middleColor)) > 40):
                self.rightXborder = x            
                break
        for y in range(self.yCenter,1,-5):
            if(abs(int(surfaceMatrix[y][self.xCenter]) - int(self.middleColor)) > 40):
                self.upperYborder = y
                break            
        for y in range(self.yCenter,len(surfaceMatrix)-1, 5):
            if(abs(int(surfaceMatrix[y][self.xCenter]) - int(self.middleColor)) > 40):
                self.lowerYborder = y
                break    

    def findPointInBall(self, surfaceMatrix):
            #print("middle color is", self.middleColor)
            for y in range(self.upperYborder+80, self.lowerYborder-80, 10):
                for x in range(self.leftXborder +80 , self.rightXborder -80 , 10 ):
                    if(abs(int(surfaceMatrix[y][x]) - int(self.middleColor)) > 120):
                        if((abs(int(surfaceMatrix[y+self.delta][x+self.delta]) - int(self.middleColor)) > 120) and (abs(int(surfaceMatrix[y+self.delta][x-self.delta]) - int(self.middleColor)) > 120) and (abs(int(surfaceMatrix[y-self.delta][x+self.delta]) - int(self.middleColor)) > 120) and (abs(int(surfaceMatrix[y-self.delta][x-self.delta]) - int(self.middleColor)) > 120)):
                            self.ballColor = surfaceMatrix[y][x] 
                            return Point(x,y)
            return Point(-1,-1)
        
    def findMiddleOfBall(self, point, surfaceMatrix):
        rightX=-1
        leftX=-1
        upperY = -1
        lowerY = -1
        for x in range(point.x , self.leftXborder , -2):
            if(abs(int(surfaceMatrix[point.y][x]) - self.ballColor) > 50):
                leftX = x
                break
        for x in range(point.x , self.rightXborder, 2  ):
            if(abs(int(surfaceMatrix[point.y][x]) - self.ballColor) > 50):
                rightX = x
                break
        for y in range(point.y , self.upperYborder , -2 ):
            if(abs(int(surfaceMatrix[y][point.x]) - self.ballColor) > 50):
                upperY = y
                break
        for y in range(point.y , self.lowerYborder, 2  ):
            if(abs(int(surfaceMatrix[y][point.x]) - self.ballColor) > 50):
                lowerY = y
                break
        middleX_coordinate =int((rightX + leftX)/2 )
        middleX_coordinate = middleX_coordinate - self.xCenter
        middleY_coordinate = int((upperY + lowerY)/2)
        middleY_coordinate = middleY_coordinate - self.yCenter
        return Point(middleX_coordinate, -middleY_coordinate)
                

    def __str__(self):
        return (f'Surface('
                f'upperYborder={self.upperYborder}, '
                f'lowerYborder={self.lowerYborder}, '
                f'middleColor={self.middleColor}, '
                f'rightXborder={self.rightXborder}, '
                f'leftXborder={self.leftXborder}, '
                f'ballColor={self.ballColor})')

