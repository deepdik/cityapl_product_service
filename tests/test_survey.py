import json
import os
import unittest

from app import app


class SurveyTestCase(unittest.TestCase):
	"""This class represents the survey test case"""

	def setUp(self):
		"""Define test variables and initialize app."""
		self.app = app
		self.client = self.app.test_client
		# binds the app to the current context
		# with self.app.app_context():
			# create all tables
			
	def test_homepage(self):
		"""
		"""
		res = self.client().get('/api/v1/home/')
		self.assertEqual(res.status_code, 200)

	def test_create_survey(self):
		"""
		"""
		res = self.client().post('/api/v1/survey/', data={})
		self.assertEqual(res.status_code, 200)


	def tearDown(self):
		"""teardown all initialized variables."""
		# with self.app.app_context():
			# drop all tables
		pass

# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()