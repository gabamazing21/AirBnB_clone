#!/usr/bin/python3
import uuid
from datetime import datetime
from . import storage
"""BaseModel """


class BaseModel():
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop("name", None)
        self.my_number = kwargs.pop("my_number", None)
        if kwargs:
            for keys, value in kwargs.items():
                if keys == "created_at":
                    value = datetime.fromisoformat(value)
                    setattr(self, keys, value)
                if keys == "updated_at":
                    value = datetime.fromisoformat(value)
                    setattr(self, keys, value)
                if keys != "__class__":
                    setattr(self, keys, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ string representation of the class """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """ update updated_at attribute with current time"""
        updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ return dictionary of class attribute """
        class_property = {}
        class_property["id"] = self.id
        class_property["__class__"] = "BaseModel"
        if self.name is not None:
            class_property["name"] = self.name
        if self.my_number is not None:
            class_property["my_number"] = self.my_number
        class_property["created_at"] = self.created_at.isoformat()
        class_property["updated_at"] = self.updated_at.isoformat()
        return class_property
