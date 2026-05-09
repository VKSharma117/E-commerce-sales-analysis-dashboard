CREATE DATABASE superstore;

USE superstore;

SELECT * FROM superstore_csv LIMIT 10;

SELECT Category, SUM(Profit) AS total_profit
FROM superstore_csv
GROUP BY Category
ORDER BY total_profit DESC;

SELECT `Sub-Category`, SUM(Profit) AS total_profit
FROM superstore_csv
GROUP BY `Sub-Category`
ORDER BY total_profit DESC;

SELECT `Product Name`, SUM(Profit) AS total_profit
FROM superstore_csv
GROUP BY `Product Name`
HAVING total_profit < 0
ORDER BY total_profit ASC;

SELECT Region,
SUM(Sales) AS total_sales,
SUM(Profit) AS total_profit
FROM superstore_csv
GROUP BY Region
ORDER BY total_profit DESC;

SELECT State, SUM(Profit) AS total_profit
FROM superstore_csv
GROUP BY State
ORDER BY total_profit DESC
LIMIT 5;

SELECT Discount, AVG(Profit) AS avg_profit
FROM superstore_csv
GROUP BY Discount
ORDER BY Discount;

SELECT 
MONTH(`Order Date`) AS month,
SUM(Sales) AS total_sales
FROM superstore_csv
GROUP BY month
ORDER BY month;

SELECT `Product Name`, SUM(Sales) AS total_sales
FROM superstore_csv
GROUP BY `Product Name`
ORDER BY total_sales DESC
LIMIT 10;

SELECT Segment,
SUM(Sales) AS total_sales,
SUM(Profit) AS total_profit
FROM superstore_csv
GROUP BY Segment
ORDER BY total_profit DESC;

SELECT Category,
SUM(Profit)/SUM(Sales) AS profit_margin
FROM superstore_csv
GROUP BY Category
ORDER BY profit_margin DESC;

SELECT City, SUM(Sales) AS total_sales
FROM superstore_csv
GROUP BY City
ORDER BY total_sales DESC
LIMIT 10;
