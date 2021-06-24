from apps.product.views import Product, ProductDetailView, CategoryView


def initialize_routes(api):
	"""
	"""
	api.add_resource(Product, '/product/')
	api.add_resource(ProductDetailView, '/product/<product_id>/')
	api.add_resource(CategoryView, '/category/')
