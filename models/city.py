#!/usr/bin/python3
""" City Module """
from models.base_model import BaseModel
class City(BaseModel):
    """ city class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """City instance"""
        super.__init__(*args, **kwargs)

