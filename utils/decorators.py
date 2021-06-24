from functools import wraps
from flask import g, request, redirect, url_for
from flask_restful import abort


def authenticate(func):
	"""
	"""
	@wraps(func)
	def wrapper(*args, **kwargs):
		if not getattr(func, 'authenticated', True):
			return func(*args, **kwargs)

		# custom account lookup function
		# acct = basic_authentication()
		# if acct:
		# 	return func(*args, **kwargs)

		abort(401)
	return wrapper
