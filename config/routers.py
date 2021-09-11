from apps.product.views import (Product,
	ProductDetailView, CategoryView, CategorySubcategoryView,
	VerticalAttributesView)


def initialize_routes(api):
	"""
	"""
	api.add_resource(Product, '/product/')
	api.add_resource(ProductDetailView, '/product/<int:product_id>/')
	api.add_resource(CategoryView, '/category/')
	api.add_resource(CategorySubcategoryView, '/category-subcat-vertical/')
	api.add_resource(VerticalAttributesView, '/vertical/<int:vertical_id>/attributes/')
