#!/usr/bin/python3
"""Write the first class Base:"""
import json
from os import path


class Base:
    """Class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Inicialice class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string"""
        if list_dictionaries is None:
            list_dictionaries = []
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation"""
        obj = []
        if list_objs:
            for i in list_objs:
                obj.append(cls.to_dictionary(i))
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(obj))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            from models.rectangle import Rectangle
            object = Rectangle(1, 1)
        elif cls.__name__ is "Square":
            from models.square import Square
            object = Square(1)
        object.update(**dictionary)
        return object

    @classmethod
    def load_from_file(cls):
        """returns a list"""
        if not path.isfile(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

