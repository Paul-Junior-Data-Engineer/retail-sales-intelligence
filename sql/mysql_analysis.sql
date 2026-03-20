-- ============================================
-- RETAIL SALES SQL ANALYSIS
-- ============================================

USE retail_sales;

-- ============================================
-- 1. TOTAL SALES & PROFIT OVERVIEW
-- ============================================

SELECT
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(AVG(profit_margin), 2) AS avg_profit_margin
FROM sales_data;


-- ============================================
-- 2. SALES BY REGION
-- ============================================

SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY region
ORDER BY total_sales DESC;


-- ============================================
-- 3. SALES TREND (MONTHLY)
-- ============================================

SELECT
    order_year,
    order_month,
    ROUND(SUM(sales), 2) AS monthly_sales,
    ROUND(SUM(profit), 2) AS monthly_profit
FROM sales_data
GROUP BY order_year, order_month
ORDER BY order_year, order_month;


-- ============================================
-- 4. CATEGORY PERFORMANCE
-- ============================================

SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(AVG(profit_margin), 2) AS avg_profit_margin
FROM sales_data
GROUP BY category
ORDER BY total_sales DESC;


-- ============================================
-- 5. SUB-CATEGORY ANALYSIS
-- ============================================

SELECT
    sub_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY sub_category
ORDER BY total_sales DESC
LIMIT 10;


-- ============================================
-- 6. TOP 10 CUSTOMERS BY SALES
-- ============================================

SELECT
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;


-- ============================================
-- 7. LOW PROFIT / LOSS-MAKING ORDERS
-- ============================================

SELECT
    order_id,
    customer_name,
    sales,
    profit
FROM sales_data
WHERE profit < 0
ORDER BY profit ASC
LIMIT 20;


-- ============================================
-- 8. DISCOUNT IMPACT ON PROFIT
-- ============================================

SELECT
    discount,
    ROUND(AVG(profit), 2) AS avg_profit,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales_data
GROUP BY discount
ORDER BY discount;


-- ============================================
-- 9. TOP PERFORMING STATES
-- ============================================

SELECT
    state,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales_data
GROUP BY state
ORDER BY total_sales DESC
LIMIT 10;


-- ============================================
-- 10. SEGMENT-WISE PERFORMANCE
-- ============================================

SELECT
    segment,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY segment
ORDER BY total_sales DESC;


-- ============================================
-- 11. SHIPPING MODE ANALYSIS
-- ============================================

SELECT
    ship_mode,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(AVG(profit), 2) AS avg_profit
FROM sales_data
GROUP BY ship_mode
ORDER BY total_sales DESC;


-- ============================================
-- 12. PROFITABLE VS NON-PROFITABLE ORDERS
-- ============================================

SELECT
    CASE
        WHEN profit > 0 THEN 'Profitable'
        ELSE 'Loss'
    END AS profit_status,
    COUNT(*) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales_data
GROUP BY profit_status;