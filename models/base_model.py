#!/usr/bin/python3
import uuid
from datetime import datetime
"""BaseModel """


class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.data = {}
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

    def __str__(self):
        """ string representation of the class """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """ update updated_at attribute with current time"""
        updated_at = datetime.now()

    def to_dict(self):
        """ return dictionary of class attribute """
        class_property = {}
        class_property["id"] = self.id
        class_property["__class__"] = "BaseModel"
        class_property["name"] = self.name
        class_property["my_number"] = self.my_number
        class_property["created_at"] = self.created_at.isoformat()
        class_property["updated_at"] = self.updated_at.isoformat()
        return class_property
