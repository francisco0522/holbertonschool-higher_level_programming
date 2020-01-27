#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height ))

    def update(self, *args, **kwargs):
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            elif i == 1:
                self.width = j
            elif i == 2:
                self.height = j
            elif i == 3:
                self.x = j
            elif i == 4:
                self.y = j
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "width" in kwargs:
            self.width = kwargs["width"]
        if "height" in kwargs:
            self.height = kwargs["height"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]
    
