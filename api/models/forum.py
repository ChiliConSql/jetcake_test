from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from .base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False, unique=True)
    name = Column(String(128), nullable=False, unique=True)

    def __init__(self, email, name):
        self.email = email
        self.name = name

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String(256), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='questions')

    def __init__(self, question, user_id):
        self.question = question
        self.user_id = user_id

class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    answer = Column(Text(), nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    question = relationship('Question', backref='answers')
    UniqueConstraint('question_id', 'answer')

class Bookmark(Base):
    __tablename__ = 'bookmarks'

    id = Column(Integer, primary_key=True)
    buri = Column(String(128), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='bookmarks')

