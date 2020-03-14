" endpoints for engaging in questions and answers "
import hug

@hug.post('/questions')
def post_question():
    """pose a question to the community
    sample jason -> {"question": "How many calories in a bucket of chicken"
    """
    return {
            "message": "your question has been posted",
            "question_url": "https://jetcake.com/api/questions/7",
        }

@hug.post('/answers')
def answer_question(question_id: hug.types.number, answer):
    """answer a question
    sample json = {"question_id":1, "answer": "peanut butter and bananas"}
    """
    return {
            "message": "successfully answered the question",
            "answer_url": "https://jetcake.com/api/answers/10"
        }

@hug.get('/questions')
def get_questions():
    """return all questions on feed"""
    return {
            "data": [
                {"id": 1, "question": "What is the best diet for children", },
                {"id": 2, "question": "What is the diet for grownups", },
            ]
        }

@hug.get('/answers', examples='qid=1')
def get_answers(qid: hug.types.number):
    """returns answers to questions posed by users
    pass the question id in the query string
    """
    return {
            "data": [
                {"id": 1, "answer": "carrots and peas", },
                {"id": 2, "answer": "chicken and biscuits", },
            ]
        }

@hug.post('/bookmarks')
def add_bookmark():
    """add a bookmark to a question or answer
    sample json input -> {"url": "https://jetcake.com/api/answers/2"}
    """
    return {
            "message": "this link has been bookmarked",
            "bookmark_link": "https://jetcake.com/api/bookmarks/3"
        }
