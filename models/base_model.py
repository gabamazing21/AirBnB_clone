#!/usr/bin/python3
"""BaseModel """
import uuid
from datetime import datetime
from . import storage


class BaseModel():
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """BaseModel Instance"""
        if kwargs:
            self.__dict__.update({key: value for key, value
                                  in kwargs.items()
                                  if key != "__class__"})
            self.__dict__["created_at"] = (datetime.fromisoformat
                                           (self.__dict__["created_at"]))
            self.__dict__["updated_at"] = (datetime.fromisoformat
                                           (self.__dict__["updated_at"]))

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
        class_property = self.__dict__.copy()
        class_property['__class__'] = self.__class__.__name__
        class_property['created_at'] = self.created_at.isoformat()
        class_property['updated_at'] = self.updated_at.isoformat()
        return class_property
