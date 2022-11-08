SELECT notebooks_brand.title, COUNT(brand_id) as count
FROM 
	notebooks_brand	INNER JOIN notebooks_notebook
	ON notebooks_notebook.brand_id = notebooks_brand.id
GROUP BY 1
ORDER BY 2 DESC