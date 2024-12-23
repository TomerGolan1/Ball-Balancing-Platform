import math

class Point:
    def __init__(self, x=0, y=0):
        """
        Initialize a new point at the given coordinates.

        :param x: The x-coordinate of the point.
        :param y: The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a string representation of the point.
        """
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):
        """
        Calculate the distance from this point to another point.

        :param other: Another Point instance.
        :return: The Euclidean distance between the two points.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)