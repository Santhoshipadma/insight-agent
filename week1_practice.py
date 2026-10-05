"""
Week 1 practice: Python basics -> pandas -> SQL.
Run it:  python week1_practice.py
"""

import sqlite3
import pandas as pd

# PART 1: Lists and loops
cities = ["Dallas", "Denton", "Frisco", "Plano"]
print("PART 1: Cities in our data")
for city in cities:
    print("-", city)

# PART 2: Functions
def revenue(quantity, price):
    """Revenue for one order = quantity x price."""
    return quantity * price

print("\nPART 2: 3 items at $19.99 =", revenue(3, 19.99))

# PART 3: Reading a file (plain Python)
print("\nPART 3: First 3 lines of sales.csv")
with open("sales.csv") as f:
    for i, line in enumerate(f):
        if i == 3:
            break
        print(line.strip())

# PART 4: pandas
df = pd.read_csv("sales.csv")
df["revenue"] = df["quantity"] * df["price"]
print("\nPART 4: pandas - total revenue by category")
print(df.groupby("category")["revenue"].sum().sort_values(ascending=False).round(2))

# PART 5: SQL on the same data
con = sqlite3.connect("sales.db")
df.to_sql("sales", con, if_exists="replace", index=False)
query = """
SELECT customer_city,
       COUNT(*)               AS orders,
       ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
GROUP BY customer_city
ORDER BY total_revenue DESC
"""
print("\nPART 5: SQL - revenue by city")
print(pd.read_sql(query, con))
con.close()

# ---------------------------------------------------------------
# YOUR TURN (write your code below each exercise)
# ---------------------------------------------------------------
# 1. Write a function that returns "big" if revenue > 500, else "small".
# 2. Use a loop to print every order from Dallas.
# 3. Write a SQL query: which MONTH had the most revenue?
#    Hint: substr(order_date, 1, 7) gives "2026-01"
# 4. Write a SQL query: the single most expensive order.
