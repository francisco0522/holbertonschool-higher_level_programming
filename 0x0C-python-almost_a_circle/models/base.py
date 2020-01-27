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
