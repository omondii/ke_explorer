#!/usr/bin/python3
""" Instantiates the models package 
every time the storage object is called """
from Models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()