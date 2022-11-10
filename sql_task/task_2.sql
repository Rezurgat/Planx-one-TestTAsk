SELECT CEILING(CAST(width as numeric)) + ((5 - CEILING(CAST(width as numeric)) % 5)) % 5  as width,
CEILING(CAST(depth as numeric)) + ((5 - CEILING(CAST(depth as numeric)) % 5)) % 5 as depth,
CEILING(CAST(height as numeric)) + ((5 - CEILING(CAST(height as numeric)) % 5)) % 5 as height,
COUNT(*) as count
FROM notebooks_notebook
GROUP BY 1, 2, 3
ORDER BY 1

