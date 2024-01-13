import json
import os

""" This module serialize and deseriliaze """
class FileStorage():
    """ serializes instances to a JSON file 
    and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    def new(self, obj):
        print("Let's print object before adding it to object dict: ")
        print(obj)
        key = f"{__class__.__name__}.{obj.id}"
        self.__objects.update({key:obj})
    def save(self):
        with open(self.__file_path, "w") as file:
            objects_dict = {}
            print(f"List of objects are : {self.__objects}")
            for key, value in enumerate(self.__objects):
                print(f"key: {key}")
                print(f"value: {value}")
                key.to_dict()
                objects_dict[key] = value.to_dict()
            print("print list of object before serializing it:  ")
            print(objects_dict)
            json.dump(objects_dict, file)
    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as fi:
                data = json.load(fi)
                self.__objects = data
        else:
            pass
