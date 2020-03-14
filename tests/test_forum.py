import hug
from falcon import HTTP_200

from api.app import app as jetcake
from . import ForumAPITest

class ForumTestCase(ForumAPITest):

    def setUp(self):
        super(ForumAPITest, self).setUp()

    def tearDown(self):
        # delete all users except base user
        super(ForumAPITest, self).tearDown()

    def test_can_post_question(self):
        response = hug.test.post(jetcake, "forum/questions", {"question":"Is pudding fattening"})
        assert response.status == HTTP_200
        assert response.data is not None

    def test_can_answer_question(self):
        response = hug.test.post(jetcake, "forum/answers", {"question_id": 1, "answer":"Yes, pudding is fattening"})
        assert response.status == HTTP_200
        assert response.data is not None

    def test_can_view_question(self):
        response = hug.test.get(jetcake, "forum/questions")
        assert response.status == HTTP_200
        assert response.data is not None

    def test_can_view_responses(self):
        response = hug.test.get(jetcake, "forum/answers", {"qid": 1})
        assert response.status == HTTP_200
        assert response.data is not None

    def test_can_bookmark_posts(self):
        response = hug.test.post(jetcake, "forum/bookmarks")
        assert response.status == HTTP_200
        assert response.data is not None

