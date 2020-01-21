#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        str1 = "[" + str(self.__class__.__name__) + "] "
        str1 += str(self.__size) + "/" + str(self.__size)
        return str1
