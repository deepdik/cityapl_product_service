"""
"""

get_all_active_brands = '''
	
	SELECT 
		*
 	FROM brands
 	WHERE isActive=1
 	'''

get_attributes_by_vertical = '''

	SELECT
	 	a."id",
	 	a."verticalName",
	 	attributes as "vericalAttributes",
		a."brands" as "brands"
	FROM (
		SELECT 
			vertical.*,
			json_agg(
				json_build_object(
					'id', 			brands."id",
					'brandName', 	brands."brandName",
					'isActive', 	brands."isActive" 
				)
			) as brands
		FROM vertical
		FULL OUTER JOIN brands
		ON vertical."createdAt" != brands."createdAt"
		WHERE brands."isActive"=true
		GROUP by vertical."id"
	) AS a
	LEFT JOIN (
		SELECT 
			b."verticalId",
			json_agg(
				json_build_object(
					'id',			    b."id",
					'attribute_name',   b."attribute_name",
					'displayName',    	b."displayName",
					'fieldType',   		b."fieldType",
					'isRequired',   	b."isRequired",
					'isMultiselect',    b."isMultiselect",
					'options',   		b."options"
				)
			) AS  attributes
		FROM attribute AS b
		GROUP BY b."verticalId"
		) AS b
	ON a."id" = b."verticalId"
	WHERE a."id" = %s
	'''

get_cat_sub_vert = '''

	SELECT 
		a."categoryName",
		a."id",
        a."isActive",
        subcategories AS "subcategories"
	From category AS a
	LEFT JOIN (
		SELECT 
			b."categoryId",
			json_agg(
				json_build_object(
					'subCategoryName',  b."subCategoryName",
					'id',			    b."id",
					'subCatImg',        b."subCatImg",
					'isActive', 		b."isActive",
					'verticals',        verticals 
				)
			) AS subcategories 
		FROM subcategory AS b
		LEFT JOIN (
			SELECT 
				c."subCategoryId",
				json_agg(
					json_build_object(
						'verticalName',  c."verticalName",
						'id',			 c."id", 
						'verticalImg',   c."verticalImg",
						'isActive',      c."isActive"
					)
				) AS verticals 
			FROM vertical AS c
		GROUP BY c."subCategoryId") AS c
		ON b."id" = c."subCategoryId"
	GROUP BY b."categoryId") AS b
	ON a."id" = b."categoryId"
	'''
