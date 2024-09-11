# Global Electronics Dashboard and Sales Data Analysis Project

## Overview
This project involves the cleaning, processing, and analysis of global electronics sales data and creating an interactive dashboard for Global Electronics using their cleaned data. It includes scripts for data cleaning in Python ,SQL queries for insights generation and dashboard powerbi file, which can be used in tools like Power BI for visualization and further analysis.

## Project Structure
The project consists of two main components:

1. `cleaning_code.py`: Python script for data cleaning and preprocessing
2. `insights_sql.py`: SQL queries for data analysis and insights generation
3. `global_elec_dashboard.pbix`: File contains working dashboard 
## Data Cleaning (`cleaning_code.py`)

This script cleans and preprocesses several datasets:

- Exchange Rates
- Products
- Sales
- Customers
- Stores

### Key Operations:
- Data type conversions
- Handling missing values
- Removing duplicates
- Creating derived columns
- Merging datasets

### Outputs:
- `exchange_cleaned.csv`
- `products_cleaned.csv`
- `sales_cleaned.csv`
- `customers_cleaned.csv`
- `stores_cleaned.csv`

## Data Analysis (`insights_sql.py`)

This file contains SQL queries for extracting insights from the cleaned data. These queries can be used in Power BI or other SQL-compatible tools.

### Key Insights:
- Sales quantity and profit trends over years
- Monthly trends in quantity sold and profit
- Year-over-year comparison of January and February sales
- Customer demographics breakdown
- Product color performance
- Store performance analysis
- Currency impact on profits

## How to Use

1. **Data Cleaning:**
   - Ensure you have Python and the required libraries (pandas, matplotlib) installed.
   - Place the raw CSV files in the same directory as the script.
   - Run `cleaning_code.py` to generate cleaned CSV files.

2. **Data Analysis:**
   - Use the SQL queries in `insights_sql.py` with your preferred SQL database or business intelligence tool (e.g., Power BI).
   - Copy and paste the relevant SQL queries to generate the desired insights.

## Requirements
- Python 3.x
- pandas
- matplotlib
- SQL-compatible database or BI tool (e.g., Power BI)

## Notes
- Ensure that your data files match the expected structure in the cleaning script.
- Some queries may need to be adapted based on your specific database schema or tool requirements.

## Future Improvements
- Automate the entire process from cleaning to analysis
- Implement error handling and logging in the Python script
- Create a configuration file for easily adjustable parameters
- Develop a dashboard template for Power BI using these queries
