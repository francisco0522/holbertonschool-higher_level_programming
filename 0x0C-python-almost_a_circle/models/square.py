#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Write the class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """"inicialization constructor"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """property function"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        """should print, and str() should return"""
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.__size))

    def update(self, *args, **kwargs):
        """update"""
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            elif i == 1:
                self.size = j
            elif i == 2:
                self.x = j
            elif i == 3:
                self.y = j
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]
