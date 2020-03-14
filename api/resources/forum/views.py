" endpoints for engaging in questions and answers "
import hug

@hug.post('/questions')
def post_question():
    """pose a question to the community
    sample jason -> {"question": "How many calories in a bucket of chicken"
    """
    msg = 'failed operation'
    qurl = None
    new_id = None
    if new_id:
        msg = "your question has been posted"
        qurl = f"https://jetcake.com/api/questions/{new_id}"

    return {
            "message": msg,
            "question_url": qurl,
        }

@hug.post('/answers')
def answer_question(question_id: hug.types.number, answer):
    """answer a question
    sample json = {"question_id":1, "answer": "peanut butter and bananas"}
    """
    msg = 'failed operation'
    ansurl = None
    new_id = None
    if new_id:
        msg = "successfully answered the question"
        ansurl = f"https://jetcake.com/api/answers/{new_id}"

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
    if questions:
        msg = "here are the questions"
    return {
            "message": msg,
            "questions": questions
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
    answers = []
    msg = 'failed operation'
    if answers:
        msg = 'here are the answers'
    return {
            "message": msg,
            "answers": answers
        }

@hug.post('/bookmarks')
def add_bookmark():
    """add a bookmark to a question or answer
    sample json input -> {"url": "https://jetcake.com/api/answers/2"}
    """
    msg = 'failed operation'
    blink = None
    blink_id = None
    if blink_id:
        blink = f"https://jetcake.com/api/bookmarks/{blink_id}"
        msg = "this link has been bookmarked"
    return {
            "message": msg,
            "bookmark_link": blink
        }
