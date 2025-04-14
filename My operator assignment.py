# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 19:32:15 2025

@author: dell
"""
#My Opertor assignment_Aman


import pandas as pd

# Load the uploaded CSV file
file_path = R"C:\Users\dell\Desktop\Projects\Python\sales_data (2).csv"
df = pd.read_csv(file_path)

# Display basic information and the first few rows of the dataset
df.info(), df.head()


# Convert 'Date' column to datetime and extract additional time-based features
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
df['Day'] = df['Date'].dt.day_name()
df['Hour'] = pd.to_datetime(df['Time']).dt.hour

# Initial aggregations for insights
sales_by_month = df.groupby('Month')['Total'].sum().sort_values(ascending=False)
sales_by_product = df.groupby('Product line')['Total'].sum().sort_values(ascending=False)
sales_by_branch = df.groupby('Branch')['Total'].sum().sort_values(ascending=False)
sales_by_payment = df['Payment'].value_counts()
customer_type_distribution = df['Customer type'].value_counts()
gender_distribution = df['Gender'].value_counts()
average_rating_by_product = df.groupby('Product line')['Rating'].mean().sort_values(ascending=False)

# Prepare a summary dictionary
summary = {
    "Sales by Month": sales_by_month,
    "Sales by Product Line": sales_by_product,
    "Sales by Branch": sales_by_branch,
    "Sales by Payment Method": sales_by_payment,
    "Customer Type Distribution": customer_type_distribution,
    "Gender Distribution": gender_distribution,
    "Average Rating by Product Line": average_rating_by_product
}

summary




# 1. Hourly Sales Trend
hourly_sales = df.groupby('Hour')['Total'].sum().sort_index()

# 2. Sales by Day of the Week
weekday_sales = df.groupby('Day')['Total'].sum().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

# 3. Average Spend by Gender
avg_spend_gender = df.groupby('Gender')['Total'].mean()

# 4. Average Spend by Customer Type
avg_spend_customer_type = df.groupby('Customer type')['Total'].mean()

# 5. Correlation between Rating and Total Purchase
correlation_rating_total = df[['Rating', 'Total']].corr().loc['Rating', 'Total']

# 6. Top 3 Product Lines in Each Branch
top_products_by_branch = (
    df.groupby(['Branch', 'Product line'])['Total']
    .sum()
    .sort_values(ascending=False)
    .groupby(level=0)
    .head(3)
)
