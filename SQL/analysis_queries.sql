-- Query 1: Sales and profit by region
SELECT
  Region,
  ROUND(SUM(Sales), 2) AS total_sales,
  ROUND(SUM(Profit), 2) AS total_profit,
  COUNT(*) AS total_orders
FROM orders
GROUP BY Region
ORDER BY total_sales DESC;

-- Query 2: Sales and profit by category
SELECT
  Category,
  ROUND(SUM(Sales), 2) AS total_sales,
  ROUND(SUM(Profit), 2) AS total_profit,
  COUNT(*) AS total_orders
FROM orders
GROUP BY Category
ORDER BY total_sales DESC;

-- Query 3: Monthly sales/profit trend
SELECT
  Order_Year,
  Order_Month,
  ROUND(SUM(Sales), 2) AS total_sales,
  ROUND(SUM(Profit), 2) AS total_profit
FROM orders
GROUP BY Order_Year, Order_Month
ORDER BY Order_Year, Order_Month;

-- Query 4: Top sub-categories by sales
SELECT
  "Sub-Category" AS Sub_Category,
  ROUND(SUM(Sales), 2) AS total_sales,
  ROUND(SUM(Profit), 2) AS total_profit,
  COUNT(*) AS total_orders
FROM orders
GROUP BY "Sub-Category"
ORDER BY total_sales DESC
LIMIT 10;