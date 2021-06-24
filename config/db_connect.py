import os
from utils import pylogger

from flask import Flask
from flask_pymongo import PyMongo


class DBConnector:
	"""
	Singleton class for database connection
	"""
	__instance = None

	@classmethod
	def connect_with_pool(cls, app):
		""" 
		static method to get instance
		"""
		if not cls.__instance:
			print('new')
			cls.__instance = cls.__start_pool(app)
		return cls.__instance

	@staticmethod
	def __start_pool(app):
		"""
		"""
		app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
		mongo = PyMongo(app)
		return mongo
