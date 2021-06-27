import json

from flask import Blueprint
from flask import request, jsonify
from flask_restful import Resource
from bson.json_util import dumps
from bson import ObjectId

from app import mongo, postgres
from config.db_connect import PostgresExcecuteQuery
from utils import pylogger
from utils.decorators import authenticate
from .queries import *
from flask import jsonify, make_response


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
		print(data)
		mongo.db.Category.insert_many(data)
		return jsonify({'message':'success'})


class CategorySubcategoryView(Resource):
	"""
	"""
	def get(self):
		"""
		"""
		data = PostgresExcecuteQuery.fetch_data(postgres, get_cat_sub_vert)
		return make_response(jsonify(data), 200)


class VerticalAttributesView(Resource):
	"""
	"""
	def get(self, *args, **kwargs):
		"""
		"""

		vertical_id = kwargs.get('vertical_id')
		cat = PostgresExcecuteQuery.fetch_data(
			postgres,
			get_attributes_by_vertical,
			(vertical_id,)
		)
		
		return {'data': cat}, 200
