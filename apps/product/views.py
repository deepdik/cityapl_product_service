import json
from flask import Blueprint
from flask import request, jsonify
from flask_restful import Resource

from utils import pylogger
from utils.decorators import authenticate
from config.db_connect import DBConnector
from app import mongo
from bson.json_util import dumps
from bson import ObjectId


class Product(Resource):
	"""
	"""
	# method_decorators = [authenticate]
	def get(self, *args, **kwargs):
		"""
		"""
		data = list(mongo.db.product.find())
		return jsonify(data)
 
	def post(self, *args, **kwargs):
		data = []
		# logger
		data = request.json
		mongo.db.product.insert_one(data)
		return jsonify({'messsge': 'Saved successfully'})


class ProductDetailView(Resource):
	"""
	"""
	def get(self, *args, **kwargs):
		"""
		"""
		product_id = kwargs.get('product_id')
		try:
			obj_id = ObjectId(product_id)
		except:
			return {'message':'Invalid product ID'}, 400

		data = mongo.db.product.find_one({ "_id": obj_id })
		return jsonify(data)


class CategoryView(Resource):
	"""
	"""
	def get(self, *args, **kwargs):
		data = list(mongo.db.Category.find())
		return jsonify(data)

	def post(self, *args, **kwargs):
		data = request.json
		mongo.db.Category.insert_many(data)
		return jsonify({'message':'success'})

