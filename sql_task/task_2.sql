SELECT ROUND(CAST(width as numeric), -1)  as width, 
ROUND(CAST(depth as numeric), -1) as depth,
ROUND(CAST(height as numeric), -1) as height,
COUNT(*) as count
FROM notebooks_notebook
GROUP BY 1, 2, 3
ORDER BY 1

