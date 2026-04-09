import pandas as pd
import pymysql

# Load CSV
df = pd.read_csv('orders.csv')

# Connect to MySQL
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Cricket@365',
    database='yourdb'
)

cursor = conn.cursor()

# Insert data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO orders VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
conn.close()

print("Orders loaded successfully")
