"""
Diwali Sales Data Analysis
Author: Arya Madiwale
Description: Exploratory data analysis on Diwali sales dataset to understand customer behavior and sales trends.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"Diwali Sales Data.csv", encoding= 'unicode_escape')

print(df.head(3))
print(df.shape)

# ============================================ CLEANING OF DATA ==============================================

# Display data info
print(df.info())

# Drop irrelevant/empty columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# Check and drop missing values
print(pd.isnull(df).sum())
df.dropna(inplace=True)

# Convert Amount column to integer
df['Amount'] = df['Amount'].astype('int')
print(df['Amount'].dtypes)

# Print column names
print(df.columns)

# Rename column (Note: inplace=True is missing, so this won't change the DataFrame)
df.rename(columns={'Marital_Status':'Shaadi'})

# Display basic stats for selected columns
print(df[['Age', 'Orders', 'Amount']].describe())

# ============================================ EXPLORATORY DATA ANAYSIS ==============================================

# Gender-based order count
ax = sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Gender-wise total sales
sales_gender = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
print(sales_gender)
sns.barplot(x='Gender', y='Amount', data=sales_gender)
plt.show()
# INSIGHT : From above graphs we can see that most of the buyers are female and even purchacing power of females is greater than men.

# Age group distribution with gender
ax = sns.countplot(x='Age Group', data=df, hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Age group-wise total sales
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
print(sales_age)
sns.barplot(x='Age Group', y='Amount', data=sales_age)
plt.show()
# INSIGHT : From the aboue graphs we can see that most of the buyers are of age group between 26-35 years and female.

# State-wise total orders (Top 10)
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
print(sales_state)
sns.set(rc={'figure.figsize' : (15, 5)})
sns.barplot(data=sales_state, x='State', y='Orders')
plt.show()

# State-wise total sales amount (Top 10)
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
print(sales_state)
sns.set(rc={'figure.figsize' : (15, 5)})
sns.barplot(data=sales_state, x='State', y='Amount')
plt.show()
# INSIGHT : From the above graphs we can see that most of the orders and total sales amount are from UP, Mahashtra and Kerla resp.

# Marital status count
ax = sns.countplot(x='Marital_Status', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Marital status and gender-wise sales
sales_Marital_Status = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data=sales_Marital_Status, x='Marital_Status', y='Amount', hue='Gender')
plt.show()
# INSIGHT : From the above graphs we can see that most of the buyers are married (women) and they have high purchacing power.

# Occupation distribution
sns.set(rc={'figure.figsize' : (20, 5)})
ax = sns.countplot(x='Occupation', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Occupation and gender-wise sales
sales_Occupation = df.groupby(['Occupation', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(20, 5)})
sns.barplot(data=sales_Occupation, x='Occupation', y='Amount', hue='Gender')
plt.show()
# INSIGHT : From the above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector.

# Product category distribution
sns.set(rc={'figure.figsize' : (20, 5)})
ax = sns.countplot(x='Product_Category', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Product category-wise sales (Top 10)
sales_Product_Category = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20, 5)})
sns.barplot(data=sales_Product_Category, x='Product_Category', y='Amount')
plt.show()
# INSIGHT : From the above graphs we can see that most of the sold products are from Food, Clothing and Electronics category.

# Top 10 selling products by order count
sales_Product_ID = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20, 5)})
sns.barplot(data=sales_Product_ID, x='Product_ID', y='Orders')
plt.show()

# FINAL INSIGHT:
# Married women aged 26–35 from UP, Maharashtra, and Kerala working in IT, Healthcare, and Aviation 
# are most likely to purchase food, clothing, and electronics.
