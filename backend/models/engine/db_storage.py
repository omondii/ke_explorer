#!/usr/bin/python3
"""" Database management configuration """
import models
from models import tables, base_model
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.tables import User, Categories, Comments, Article
from models.base_model import BaseModel, Base


classes = {"User": User, "Categories": Categories,
           "Article": Article, "Comments": Comments}

class DBStorage:
    """ Creates the connection to MySql """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiate a DBstorage object """
        self.__engine = create_engine("mysql+mysqldb://devbrian:exploreKe_pwd@localhost/exploreKe_db",
                                      pool_pre_ping=True)
        
    def all(self, cls=None):
        """ Query the current db session """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' +  obj.id
                    new_dict[key] = obj
        return (new_dict)
    
    def reload(self):
        """ Reload data from the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
    
    def new(self, obj):
        """ Add a new obj to the current db session """
        self.__session.add(obj)

    def save(self):
        """ Commit/save all changes of the current db session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete provided obj from the current db session """
        if obj is not None:
            self.__session.delete(obj)

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None
    
    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()