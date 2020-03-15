from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from .base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(128), nullable=False, unique=True)
    name = Column(String(128), nullable=False, unique=True)

    def __init__(self, email, name):
        self.email = email
        self.name = name

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String(256), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='questions')

    def serialize(self):
        return {
                'id': self.id,
                'qustion': self.question,
                'user_id': self.user_id,
                }

    def __init__(self, question, user_id):
        self.question = question
        self.user_id = user_id

class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    answer = Column(Text(), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='answers')
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    question = relationship('Question', backref='answers')
    UniqueConstraint('question_id', 'answer')

    def __init__(self, answer, question_id, user_id):
        self.answer = answer
        self.question_id = question_id
        self.user_id = user_id

    def serialize(self):
        return {
                'id': self.id,
                'qustion_id': self.question_id,
                'user_id': self.user_id,
                'answer': self.answer,
                }

class Bookmark(Base):
    __tablename__ = 'bookmarks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    buri = Column(String(128), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='bookmarks')

    def __init__(self, user_id, cat, cat_id):
        self.buri = f'forum/{cat}/{cat_id}'
        self.user_id = user_id

