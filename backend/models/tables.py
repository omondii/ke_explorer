#!/usr/bin/python3
""" Database schema for ExploreKe """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ Users Table  """
    __tablename__ = "user"
    id = Column(String(60), primary_key=True)
    name = Column(String(60), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    articles = relationship("Article", back_populates="author")
    comments = relationship("Comments", back_populates="commenter")


class Categories(BaseModel, Base):
    """ Categories Table """
    __tablename__ = "category"
    id = Column(String(60), primary_key=True)
    category = Column(String(60))
    articles = relationship("Article", back_populates="category")


class Article(BaseModel, Base):
    """ Articles/posts database """
    __tablename__ = "article"
    id = Column(String(60), primary_key=True)
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
    id = Column(String(60), primary_key=True)
    body = Column(String(1000), nullable=False)
    postDate = Column(DateTime, default=func.now())
    commenter_id = Column(String(60), ForeignKey('user.id'))
    commenter = relationship("User", back_populates="comments")
    article_id = Column(String(60), ForeignKey('article.id'))
    article = relationship("Article", back_populates="comments")


# Work on  relationships(backref, back_populate)
# Then flask routes
# Followed by rendering of queries to react
# 3 days.
    