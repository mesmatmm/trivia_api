import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', 'postgres', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'What is your favorite pet?',
            'answer': 'Cat',
            'category': '5',
            'difficulty': '3'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertEqual(data['total_questions'], len(Question.query.all()))
        self.assertTrue(data['categories'])
        # self.assertTrue(data['current_category'])

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['questions'])
        self.assertEqual(data['total_questions'], len(Question.query.all()))

    def test_405_if_question_creation_fails(self):
        res = self.client().post('/questions/45', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_delete_question(self):
        last_question_id = Question.query.order_by(
            Question.id.desc()).first().id

        res = self.client().delete(f'/questions/{last_question_id}')
        data = json.loads(res.data)

        question = Question.query.filter(
            Question.id == last_question_id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], last_question_id)
        self.assertTrue(data['questions'])
        self.assertEqual(data['total_questions'], len(Question.query.all()))
        self.assertTrue(data['categories'])
        self.assertEqual(question, None)

    def test_422_if_question_creation_fails(self):
        # will fail since this question id doesn't exist
        res = self.client().delete('/questions/2020')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_get_questions_by_category(self):
        """Tests getting questions by category success"""
        first_category = Category.query.order_by(Category.id).first()
        res = self.client().get(f'/categories/{first_category.id}/questions')
        data = json.loads(res.data)
        # check status code and success message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # make sure there's result and current category is as the selected one
        self.assertEqual(data['current_category'].get(
            'type'), first_category.type)
        self.assertIsNotNone(data['questions'])
        self.assertIsNotNone(data['total_questions'])

    def test_400_if_questions_by_category_fails(self):
        """Tests getting questions by category failure 400"""
        # send request with category id 2020
        category_id = 2020
        res = self.client().get(f'/categories/{category_id}/questions')
        data = json.loads(res.data)
        # check response status code and message
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    # tests for search
    # that check a response when there are results and when there are none

    def test_get_questions_search_with_results(self):
        searchTerm = 'what'
        search_results = Question.query.order_by(Question.id).filter(
            Question.question.ilike('%{}%'.format(searchTerm))).all()

        res = self.client().post('/questions/search',
                                 json={'searchTerm': searchTerm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], len(search_results))
        self.assertIsNotNone(data['questions'])

    def test_get_question_search_without_results(self):
        res = self.client().post(
            '/questions/search', json={'searchTerm': 'MahmoudEsmat'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], 0)
        self.assertIsNotNone(data['questions'])

        # self.assertEqual(data['questions'], [])

    def test_get_questions_quiz(self):
        json_data = {"previous_questions": [],
                     "quiz_category": {"id": 2, "type": "Art"}}
        res = self.client().post('/quizzes', json=json_data)
        data = json.loads(res.data)

        # check status code and success message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['question'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
