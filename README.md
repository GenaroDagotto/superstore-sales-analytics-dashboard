# Superstore Sales Analytics Pipeline & Dashboard

## Project Overview
This project analyzes a Superstore sales dataset using **Python, SQL (SQLite), and Power BI** to explore sales performance across regions, categories, and time.  
It combines data preparation, SQL-based analysis, and dashboard visualization to produce stakeholder-friendly business insights.

## Tools & Technologies
- **Python (pandas)** - data cleaning and preparation
- **SQLite** - SQL-based analysis and querying
- **Power BI** - interactive dashboard design and visualization
- **VS Code** - scripting and project organization
- **DB Browser for SQLite** - database exploration and SQL execution

## Project Workflow
1. **Raw Data (CSV)** imported from the Superstore dataset
2. **Python ETL script** cleans and prepares the data
3. Cleaned data is saved as:
   - `superstore_clean.csv`
   - `superstore.db` (SQLite database)
4. **SQL queries** are used to analyze trends and performance
5. **Power BI dashboard** visualizes KPIs and performance insights

## Key Features
- KPI cards for:
  - Total Sales
  - Total Profit
  - Total Orders
  - Profit Margin %
- Visual analysis by:
  - Region
  - Category
  - Time trends (monthly/yearly)
- SQL analysis queries for business reporting and validation

## Files Included
- `scripts/etl_superstore.py` - Python ETL / cleaning script
- `sql/analysis_queries.sql` - SQL queries used for analysis
- `data/processed/superstore_clean.csv` - cleaned dataset output
- `data/processed/superstore.db` - SQLite database
- `dashboard/2.1_Superstore_Formatting_Dagotto.pbix` - Power BI dashboard
- `screenshots/` - dashboard screenshots

## Skills Demonstrated
- Data cleaning and transformation
- SQL querying and aggregation
- Business intelligence dashboarding
- KPI design and reporting
- End-to-end analytics workflow (ETL + SQL + BI)

## Sample SQL Analyses
Examples included in `analysis_queries.sql`:
- Sales and profit by region
- Sales and profit by category
- Monthly sales/profit trends
- Top sub-categories by sales

## Dashboard Screenshots
(Add your screenshots here after uploading to GitHub)

## Future Improvements
- Add more DAX measures (YoY growth, average order value)
- Connect Power BI directly to SQLite database
- Add advanced filtering and drill-through pages