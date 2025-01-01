#!/usr/bin/python3
"""" Database Creation and management methods
Table must be imported and added to classes dict
"""
import os
import Models
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from Models.tables import User, Categories, Comments, Article
from Models.base_model import Base
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv('DATABASE_URL')


classes = {"User": User, "Categories": Categories,
           "Article": Article, "Comments": Comments}

class DBStorage:
    """ Creates a connection to application's MySql db """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiates the DBstorage class
        Handles db setup and common db operations"""
        self.__engine = create_engine(DB_URL, pool_pre_ping=True)
        
    def all(self, cls=None):
        """ Query the current db session for all items of a table
        returns a dict containing all items in the corresponding table """
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
        """ Returns the object based on the class name and its ID """
        if cls not in classes.values():
            return None

        all_cls = Models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def get_by_email(self, cls, email):
        """Returns the object based on the class and email"""
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        for value in all_cls.values():
            if value.email == email:
                return value
        return None

    def rollback(self):
        """
        Reverts changes made i the current session to the last commited state
        :return:
        """
        self.__session.rollback()
    
    def close(self):
        """ call remove() method on the private session attribute """
        self.__session.remove()

