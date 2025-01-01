#!/usr/bin/python3
""" Database schema for ExploreKe """
from Models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from server import app


class User(BaseModel, Base, UserMixin):
    """ Users Table  """
    __tablename__ = "user"
    id = Column(String(128), primary_key=True)
    username = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(128))
    articles = relationship("Article", back_populates="author")
    comments = relationship("Comments", back_populates="commenter")

    def __repr__(self):
        """ Format to return user details """
        return '<user {}>'.format(self.username)
    
    def set_password(self, password):
        """ Encrypt password field """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """ Check if password is encrypted """
        return check_password_hash(self.password_hash, password)
    

def load_user(id):
    return User.query.get(int(id))

class Article(BaseModel, Base):
    """ Articles/posts database """
    __tablename__ = "article"
    id = Column(String(128), primary_key=True)
    title = Column(String(20), nullable=False)
    body = Column(String(1000), nullable=False)
    author = relationship("User", back_populates="articles")
    author_id = Column(String(60), ForeignKey('user.id'))
    category = relationship("Categories", back_populates="articles")
    category_id = Column(String(60), ForeignKey('category.id'))
    comments = relationship("Comments", back_populates="article")

class Comments(BaseModel, Base):
    """ Comments Table """
    __tablename__ = "comment"
    id = Column(String(128), primary_key=True)
    body = Column(String(1000), nullable=False)
    postDate = Column(DateTime, default=func.now())
    commenter_id = Column(String(60), ForeignKey('user.id'))
    commenter = relationship("User", back_populates="comments")
    article_id = Column(String(60), ForeignKey('article.id'))
    article = relationship("Article", back_populates="comments")

class Categories(BaseModel, Base):
    """ Categories Table """
    __tablename__ = "category"
    id = Column(String(128), primary_key=True)
    category = Column(String(60))
    articles = relationship("Article", back_populates="category")

