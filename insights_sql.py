# Paste these sql commands in power Bi while data importing in the server name entry dialogue box
# To get the specified table from main data from sql to perform analysis 

# Sales Quantity and  Profit trend over the years recorded on Data
'''
SELECT 
    YEAR(`Order_Date`) AS OrderYear,  
    SUM(`Profit`) AS TotalProfit,
    SUM(`Quantity`) AS TotalQuantity
FROM 
    sales_global_elec
GROUP BY 
    YEAR(`Order_Date`)
ORDER BY 
    OrderYear;
'''

# Monthly trends in quantity sold and profit over the recorded years
'''
SELECT 
    YEAR(`Order_Date`) AS OrderYear, 
    MONTH(`Order_Date`) AS OrderMonth, 
    SUM(`Profit`) AS TotalProfit,
    SUM(`Quantity`) AS TotalQuantity
FROM 
    sales_global_elec
GROUP BY 
    YEAR(`Order_Date`), 
    MONTH(`Order_Date`)
ORDER BY 
    OrderYear, 
    OrderMonth;
'''

# 2021 vs others: January and February Sales Quantities Analysis for Performance Prediction
'''
SELECT 
    MONTH(`Order_Date`) AS OrderMonth, 
    SUM(CASE WHEN YEAR(`Order_Date`) = 2021 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2021,
    SUM(CASE WHEN YEAR(`Order_Date`) = 2020 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2020,
    SUM(CASE WHEN YEAR(`Order_Date`) = 2019 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2019,
    SUM(CASE WHEN YEAR(`Order_Date`) = 2018 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2018,
    SUM(CASE WHEN YEAR(`Order_Date`) = 2017 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2017,
    SUM(CASE WHEN YEAR(`Order_Date`) = 2016 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2016
FROM 
    sales_global_elec
WHERE 
    MONTH(`Order_Date`) IN (1, 2)
GROUP BY 
    MONTH(`Order_Date`)
ORDER BY 
    OrderMonth;
'''

# Demographic Customers Breakdown by their Age Group
'''

SELECT 
    CASE 
        WHEN Age BETWEEN 20 AND 29 THEN '20-29'
        WHEN Age BETWEEN 30 AND 39 THEN '30-39'
        WHEN Age BETWEEN 40 AND 49 THEN '40-49'
        WHEN Age BETWEEN 50 AND 59 THEN '50-59'
        WHEN Age BETWEEN 60 AND 69 THEN '60-69'
        ELSE '70+'
    END AS AgeGroup,
    COUNT(*) AS CustomerCount
FROM 
    customers_global_elec
GROUP BY 
    CASE 
        WHEN Age BETWEEN 20 AND 29 THEN '20-29'
        WHEN Age BETWEEN 30 AND 39 THEN '30-39'
        WHEN Age BETWEEN 40 AND 49 THEN '40-49'
        WHEN Age BETWEEN 50 AND 59 THEN '50-59'
        WHEN Age BETWEEN 60 AND 69 THEN '60-69'
        ELSE '70+'
    END
ORDER BY 
    AgeGroup;
'''

# Customers with No Purchase Activity
'''
SELECT c.*
FROM customers_global_elec c
LEFT JOIN sales_global_elec s ON c.CustomerKey = s.CustomerKey
WHERE s.CustomerKey IS NULL;
'''

# Sales Spectrum: Color Performance
'''
SELECT 
    p.Color,
    SUM(s.Quantity) AS TotalQuantity
FROM 
    sales_global_elec s
JOIN 
    products_global_elec p ON s.ProductKey = p.ProductKey
GROUP BY 
    p.Color
ORDER BY 
    p.Color;
'''

# Stores Without Corresponding Sales Records
'''
SELECT s.*
FROM stores_global_elec s
LEFT JOIN sales_global_elec sa ON s.StoreKey = sa.StoreKey
WHERE sa.StoreKey IS NULL;
'''

# Leading Product Categories by Sales Volume
'''
SELECT p.Category, SUM(s.Quantity) AS TotalQuantity
FROM sales_global_elec s
JOIN products_global_elec p ON s.ProductKey = p.ProductKey
GROUP BY p.Category
ORDER BY TotalQuantity DESC;
'''

# Store Performance Analysis: Insights on Total Profit
'''
SELECT s.*, sp.TotalProfit , sp.TotalQuantity
FROM stores_global_elec s
JOIN (
    SELECT StoreKey, SUM(Profit) AS TotalProfit, SUM(Quantity) AS TotalQuantity
    FROM sales_global_elec
    GROUP BY StoreKey
) sp ON s.StoreKey = sp.StoreKey;
'''

# Analyzing Average Profits in USD Across Various Currencies
'''
#Calculate the correlation coefficients between Profit and Exchange
WITH Correlation AS (
    SELECT 
        (SUM((Profit - avgProfit) * (Exchange_Rate - avgExchange)) / COUNT(*)) / 
        (SQRT(SUM(POWER(Profit - avgProfit, 2)) / COUNT(*)) * SQRT(SUM(POWER(Exchange_Rate - avgExchange, 2)) / COUNT(*))) AS CorrelationCoefficient
    FROM 
        (SELECT 
            Profit, 
            Exchange_Rate, 
            AVG(Profit) OVER () AS avgProfit, 
            AVG(Exchange_Rate) OVER () AS avgExchange
         FROM 
            sales_global_elec) AS subquery
)
#Create the correlation matrix table
SELECT 
    'Profit' AS `index`, 
    1.0 AS Profit, 
    (SELECT CorrelationCoefficient FROM Correlation) AS Exchange_Rate
UNION ALL
SELECT 
    'Exchange' AS `index`, 
    (SELECT CorrelationCoefficient FROM Correlation) AS Profit, 
    1.0 AS Exchange_Rate;
'''
# correlation based comparison bar chart
'''
#for barchart

SELECT 
    MONTH(`Order_Date`) AS OrderMonth,
    SUM(CASE WHEN YEAR(`Order_Date`) = 2021 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2021,
    SUM(CASE WHEN YEAR(`Order_Date`) = 2020 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2020,
    SUM(CASE WHEN YEAR(`Order_Date`) = 2019 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2019,
    SUM(CASE WHEN YEAR(`Order_Date`) = 2018 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2018,
    SUM(CASE WHEN YEAR(`Order_Date`) = 2017 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2017,
    SUM(CASE WHEN YEAR(`Order_Date`) = 2016 THEN `Quantity` ELSE 0 END) AS TotalQuantity_2016
FROM 
    sales_global_elec
WHERE 
    MONTH(`Order_Date`) IN (1, 2)
GROUP BY 
    MONTH(`Order_Date`)
ORDER BY 
    OrderMonth;
'''