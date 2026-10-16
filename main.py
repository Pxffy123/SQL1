# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# Hii ni kwa ajili ya marejeo yako ya kuona data (hiari kuacha au kufuta)
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# PART 2: Basic Select Filtering

# STEP 2
# Anapata employeeNumber na lastName kutoka kwa employees
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName 
    FROM employees
""", conn)


# STEP 3
# Inabadilisha mpangilio, lastName inaanza kabla ya employeeNumber
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber 
    FROM employees
""", conn)


# PART 3: Aliasing in Select

# STEP 4
# Inabadilisha jina la column ya employeeNumber kuwa 'ID' kwa kutumia alama ya AS
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""", conn)


# PART 4: CASE Function

# STEP 5
# Inachuja kazi na kuziweka kwenye kundi la "Executive" au "Not Executive" kama 'role'
df_executive = pd.read_sql("""
    SELECT *,
           CASE 
               WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' THEN 'Executive'
               ELSE 'Not Executive'
           END AS role
    FROM employees
""", conn)


# PART 5: Built-In Functions - Strings

# STEP 6
# Inatafuta urefu wa herufi za lastName kwa kutumia LENGTH()
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length 
    FROM employees
""", conn)


# STEP 7
# Inakata herufi mbili za kwanza za jobTitle kwa kutumia SUBSTR()
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
    FROM employees
""", conn)


# Hii ni kwa ajili ya kuona data ya orderDetails (hiari kuacha au kufuta)
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")


# PART 6: Built-In Functions - Numerics

# STEP 8
# Inazidisha priceEach na quantityOrdered, inaround, kisha inatafuta jumla (SUM)
sum_total_price = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_amount
    FROM orderDetails
""", conn)


# STEP 9
# Inatoa siku, mwezi, na mwaka kutoka kwenye column ya orderDate kwa kutumia strftime()
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
           strftime('%d', orderDate) AS day,
           strftime('%m', orderDate) AS month,
           strftime('%Y', orderDate) AS year
    FROM orders
""", conn)


# Close the connection
conn.close()
