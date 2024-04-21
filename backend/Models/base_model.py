#!/usr/bin/python3
""" BaseModel from which all classes will be derived 
Model methods to use when interacting with model objects
"""
from datetime import datetime
from Models import tables
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
import uuid
import pytz

timezone = pytz.timezone('Africa/Nairobi')
time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()

class BaseModel:
    """ Model class from which all objects will be created """
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.now(timezone))
    updated_at = Column(DateTime, default=datetime.now(timezone))

    def __init__(self, *args, **kwargs):
        """ Initialization of the base model 
        Objects can be created either by passed arguments or automatically
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.now(timezone)
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.now(timezone)
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(timezone)
            self.updated_at = self.created_at


    def __str__(self):
        """ String rep of the BaseModel class """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)
    
    def save(self):
        import Models
        """ updates objects update time to reflect last time of update every time 
        an object is saved """
        self.updated_at = datetime.now(timezone)
        Models.storage.new(self)
        Models.storage.save()

    def to_dict(self, save_fs=None):
        """ returns a dictionary containing all keys/values of an object """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict
    
    def delete(self):
        """ delete the current object from the storage """
        tables.storage.delete(self)