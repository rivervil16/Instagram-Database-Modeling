import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    type = Column(String(250))
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)
    total_likes = Column(String(250), nullable=False)
    total_comments = Column(String(250), nullable=False)
    user = relationship(User)

class UserFollowers(Base):
    __tablename__ = 'user_followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    follower_id = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)
    user = relationship(User)

class UserFeeds(Base):
    __tablename__ = 'user_feeds'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)
    user = relationship(User)

class PostLikes(Base):
    __tablename__ = 'post_likes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)
    post = relationship(Posts)
    user = relationship(User)

class PostComments(Base):
    __tablename__ = 'post_comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(String(2200), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)
    post = relationship(Posts)
    user = relationship(User)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')