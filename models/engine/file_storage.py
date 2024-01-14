""" This module serialize and deseriliaze """
import json
import os
import sys


class FileStorage():
    """ serializes instances to a JSON file
    and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return objects"""
        return self.__objects

    def new(self, obj):
        """add new object"""
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """save to file in json"""
        with open(self.__file_path, "w") as file:
            dicts = {}
            for obj in self.__objects.values():
                dicts[obj.id] = obj.to_dict()
            json.dump(dicts, file)

    def reload(self):
        """deserilize to dict from json file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as fi:
                data = json.load(fi)
                from ..base_model import BaseModel
                for i, j in data.items():
                    obj = BaseModel(**j)
                    self.__objects.update({i: obj})

        else:
            pass
