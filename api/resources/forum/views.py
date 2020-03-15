" endpoints for engaging in questions and answers "
import hug
import json

from api.config import db
from api.models.forum import *

@hug.post('/questions')
def post_question(body):
    """pose a question to the community
    sample jason -> {"question": "How many calories in a bucket of chicken"
    """
    msg = 'failed operation'
    qurl = None
    qstn = Question(body['question'], int(body['user_id']))
    db.session.begin()
    db.session.add(qstn)
    db.session.commit()
    if qstn.id:
        msg = "your question has been posted"
        qurl = f"https://jetcake.com/api/questions/{qstn.id}"

    return {
            "message": msg,
            "question_url": qurl,
        }

@hug.post('/answers')
def answer_question(body):
    """answer a question
    sample json = {"question_id":1, "user_id":1, "answer": "peanut butter and bananas"}
    """
    msg = 'failed operation'
    ansurl = None
    db.session.begin()
    answer = Answer(body['answer'], body['question_id'], body['user_id'])
    db.session.add(answer)
    db.session.commit()
    if answer.id:
        msg = "successfully answered the question"
        ansurl = f"https://jetcake.com/api/answers/{answer.id}"

    return {
            "message": msg,
            "answer_url": ansurl,
        }

@hug.get('/questions')
def get_questions():
    """return all questions on feed
    sample return:
            [
                {"id": 1, "question": "What is the best diet for children", },
                {"id": 2, "question": "What is the diet for grownups", },
            ]
    """
    questions = []
    msg = 'failed operation'
    questions = db.session.query(Question).all()
    if questions:
        msg = "here are the questions"
    return {
            "message": msg,
            "questions": [q.serialize() for q in questions]
        }

@hug.get('/answers', examples='qid=1')
def get_answers(qid: hug.types.number):
    """returns answers to questions posed by users
    pass the question id in the query string
    sample return
            [
                {"id": 1, "answer": "carrots and peas", },
                {"id": 2, "answer": "chicken and biscuits", },
            ]
    """
    answers = db.session.query(Answer).filter_by(question_id=qid).all()
    msg = 'failed operation'
    if answers:
        msg = 'here are the answers'
    return {
            "message": msg,
            "answers": [a.serialize() for a in answers]
        }

@hug.post('/bookmarks')
def add_bookmark(body):
    """add a bookmark to a question or answer
    sample json input -> {"url": "https://jetcake.com/api/answers/2"}
    """
    msg = 'failed operation'
    db.session.begin()
    bookmark = Bookmark(body['user_id'], body['cat'], body['cat_id'])
    db.session.add(bookmark)
    db.session.commit()
    if bookmark.id:
        msg = "this link has been bookmarked"
    return {
            "message": msg,
            "bookmark_link": bookmark.buri
        }
