import hug
from falcon import HTTP_200

from api.app import app as jetcake
from api.config import db
from api.models.forum import *
from . import ForumAPITest

class ForumTestCase(ForumAPITest):

    def setUp(self):
        super(ForumAPITest, self).setUp()
        db.session.begin()
        db.session.query(Bookmark).delete()
        db.session.query(Answer).delete()
        db.session.query(Question).delete()
        db.session.commit()

    def tearDown(self):
        # delete all users except base user
        super(ForumAPITest, self).tearDown()

    def test_can_post_question(self):
        q_count = db.session.query(Question).count()
        assert q_count == 0
        response = hug.test.post(jetcake, "forum/questions", {"question":"Is pudding fattening", "user_id": 1})
        assert response.status == HTTP_200
        q_count = db.session.query(Question).count()
        assert q_count == 1
        assert response.data['question_url'] is not None

    def test_can_answer_question(self):
        #let's add a question
        db.session.begin()
        qstn = Question('What is my weight', 1)
        db.session.add(qstn)
        db.session.commit()
        a_count = db.session.query(Answer).count()
        response = hug.test.post(jetcake, "forum/answers", {"user_id":1, "question_id": 1, "answer":"abut 230 pounds"})
        assert response.status == HTTP_200
        a_count = db.session.query(Answer).count()
        assert a_count == 1
        assert response.data['answer_url'] is not None

    def test_can_view_questions(self):
        #let's add a couple of questions
        db.session.begin()
        qstn = Question('What is my weight', 1)
        db.session.add(qstn)
        qstn = Question('What should I eat', 1)
        db.session.add(qstn)
        db.session.commit()
        q_count = db.session.query(Question).count()
        assert q_count == 2
        response = hug.test.get(jetcake, "forum/questions")
        assert response.status == HTTP_200
        assert len(response.data['questions']) == q_count

    def test_can_view_responses(self):
        #let's add a question
        db.session.begin()
        qstn = Question('What should I eat', 1)
        db.session.add(qstn)
        # let's add a user
        user = User('tester@test.com', 'Tester')
        db.session.add(user)
        db.session.commit()
        # let's add a couple of answers
        db.session.begin()
        answer = Answer('carrots and peas', qstn.id, user.id)
        db.session.add(answer)
        answer = Answer('chicken and waffles', qstn.id, user.id)
        db.session.add(answer)
        db.session.commit()
        a_count = db.session.query(Answer).count()
        assert a_count == 2
        response = hug.test.get(jetcake, "forum/answers", {"qid": 1})
        assert response.status == HTTP_200
        assert len(response.data['answers']) == a_count

    def test_can_bookmark_post(self):
        import re
        #let's add a question
        db.session.begin()
        qstn = Question('What should I eat', 1)
        db.session.add(qstn)
        db.session.commit()
        b_count = db.session.query(Bookmark).count()
        assert b_count == 0
        response = hug.test.post(jetcake, "forum/bookmarks",
                {'user_id': 1, 'cat': 'questions', 'cat_id':qstn.id})
        assert response.status == HTTP_200
        b_count = db.session.query(Bookmark).count()
        assert b_count == 1
        assert re.search(f'questions/{qstn.id}$', response.data['bookmark_link'])

