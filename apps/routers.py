from utils.utils import include_routers


def initialize_routes(api):
	"""
	Include all app routes
	"""
	include_routers('apps.product.routers', api)