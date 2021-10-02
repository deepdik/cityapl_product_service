"""
"""

get_all_active_brands = '''
	SELECT 
		'BRAND_SELECTION' as "unitType",
		json_agg(
				json_build_object(
					'id',			   c."id",
					'brandName',       c."brandName",
					'isActive',        d."isActive"
				) )AS data
	FROM brands AS c
	INNER JOIN brand_in_vertical AS d
	ON c."id" = d."verticalId"
	WHERE d."verticalId"=%s AND d."isActive"=true
	GROUP BY d."verticalId"
 	'''

get_attributes_by_vertical = '''

	SELECT
	 	a."name" as "unitType",
		json_agg(
			json_build_object(
				'id',			    a."id",
				'attributeName',   	a."attribute_name",
				'displayName',    	a."displayName",
				'fieldType',   		a."fieldType",
				'isRequired',   	a."isRequired",
				'isMultiselect',    a."isMultiselect",
				'options',   		a."options"
			) 
		) AS data
	FROM (
		SELECT 
			c.*,
			d."name"
		FROM attribute AS c
		LEFT JOIN attribute_section as d
		ON c."sectionTypeId" = d."id"
		) AS a
	INNER JOIN attribute_in_vertical AS b
	ON b."attributeId" = a."id"
	WHERE b."verticalId" = %s
	GROUP BY a."name"
	'''

get_cat_sub_vert = '''

	SELECT 
		a."categoryName",
		a."id",
        a."isActive",
        subcategories AS "subCategories"
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
