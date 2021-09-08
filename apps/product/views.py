import json

from flask import Blueprint
from flask import request, jsonify
from flask_restful import Resource
from bson.json_util import dumps
from bson import ObjectId

from app import mongo, postgres, cache
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
		return jsonify({'data': data})
 
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
		return jsonify({'data': data})


class CategoryView(Resource):
	"""
	"""
	def get(self, *args, **kwargs):
		data = list(mongo.db.Category.find())
		return jsonify({'data':data})

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
		return {'data':data}, 200


class VerticalAttributesView(Resource):
	"""
	"""
	@cache.cached(timeout=50)
	def get(self, *args, **kwargs):
		"""
		"""
		vertical_id = kwargs.get('vertical_id')
		cat = PostgresExcecuteQuery.fetch_data(
			postgres,
			get_attributes_by_vertical,
			(vertical_id,)
		)

		data = [
					  {
					    "unitType":"BRAND_SELECTION",
					    "data":[
					                  {
					                      "id": 1,
					                      "brandName": "Apple",
					                      "isActive": true
					                  }
					              ]
					  },
				  {
				  "unitType": "ITEM_SPECIFICATION",
				  "data":[
		                 {
		                    "id": 1,
		                    "attribute_name": "Size",
		                    "displayName": "Size",
		                    "fieldType": "Select",
		                    "isRequired": true,
		                    "isMultiselect": false,
		                    "options": [
		                        "Standard",
		                        "Large",
		                        "Small"
		                    ]
		                },
		                {
		                    "id": 2,
		                    "attribute_name": "USBVersion",
		                    "displayName": "USB Version",
		                    "fieldType": "Select",
		                    "isRequired": true,
		                    "isMultiselect": false,
		                    "options": [
		                        "USB 2.0",
		                        "USB 3.0"
		                    ]
		                }
		            ]
				  },
				  {
				  "unitType": "ADD_PHOTOS",
				  "data":[]
				  },
				  {"unitType":"MOQ_PRICE_GST_CESS",
				    "data":[
		                {
		                    "id": 1,
		                    "attribute_name": "MOQ",
		                    "displayName": "MOQ",
		                    "fieldType": "Input",
		                    "isRequired": true,
		                    "isMultiselect": false,
		                    "options": []
		                },
		                {
		                    "id": 2,
                    "attribute_name": "PRICE",
                    "displayName": "PRICE",
                    "fieldType": "Input",
                    "isRequired": true,
                    "isMultiselect": false,
                    "options": []
                },
                {
                    "id": 3,
                    "attribute_name": "GST",
                    "displayName": "GST",
                    "fieldType": "DropDown",
                    "isRequired": true,
                    "isMultiselect": false,
                    "options": ["18%","13%","12%"]
                },
                {
                    "id": 3,
                    "attribute_name": "CESS",
                    "displayName": "CESS",
                    "fieldType": "DropDown",
                    "isRequired": true,
                    "isMultiselect": false,
                    "options": ["18%","13%","12%"]
                }
            ]
			  },
			  
			  {"unitType":"GEO_RESTRICTION",
			    "data":["Banglore","Patna","Manali","Singapore"]
			  }

			]
				
		return {'data': data}, 200
