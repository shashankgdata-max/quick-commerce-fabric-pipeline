import pymysql
from pymongo import MongoClient

# -------- MySQL (Orders) --------
mysql_conn = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="testdb"
)

cursor = mysql_conn.cursor()
cursor.execute("SELECT * FROM orders")

rows = cursor.fetchall()

print("Sample Orders Data:")
for row in rows[:5]:
    print(row)


# -------- MongoDB (Inventory) --------
client = MongoClient("mongodb://localhost:27017/")
db = client["quick_commerce"]

collection = db["inventory"]

print("\nSample Inventory Data:")
for doc in collection.find().limit(5):
    print(doc)
