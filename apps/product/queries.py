"""
"""

get_all_active_brands = '''
	SELECT 
		'BRAND_SELECTION' as "unitType",
		"verticalId",
		json_agg(
				json_build_object(
					'id',			   c."id",
					'brandName',       c."brandName",
					'isActive',        c."isActive"
				) )AS data
	FROM brands AS c
	WHERE c."verticalId"=%s AND c."isActive"=true
	GROUP BY c."verticalId"
 	'''

get_attributes_by_vertical = '''
	SELECT
	 	b.*
	FROM vertical as a
	LEFT JOIN (
		SELECT 
			d."name" as "unitType",
			c."verticalId" as "verticalId",
			json_agg(
					json_build_object(
						'id',			    c."id",
						'attributeName',   	c."attribute_name",
						'displayName',    	c."displayName",
						'fieldType',   		c."fieldType",
						'isRequired',   	c."isRequired",
						'isMultiselect',    c."isMultiselect",
						'options',   		c."options"
					) 
				)AS data
		FROM attribute AS c
		LEFT JOIN attribute_section as d
		ON c."sectionTypeId" = d."id"
		GROUP BY d."name", c."verticalId"
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

# SELECT 
# 		d."name" as "UnitType",
# 		json_agg(
# 				json_build_object(
# 					'id',			    c."id",
# 					'attributeName',   	c."attribute_name",
# 					'displayName',    	c."displayName",
# 					'fieldType',   		c."fieldType",
# 					'isRequired',   	c."isRequired",
# 					'isMultiselect',    c."isMultiselect",
# 					'options',   		c."options"
# 				) )AS attt
		
# FROM attribute AS c
# LEFT JOIN attribute_section as d
# ON c."sectionTypeId" = d."id"
# GROUP BY d."name"