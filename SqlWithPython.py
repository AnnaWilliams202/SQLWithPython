import sqlite3

database = '/Users/annawilliams/Desktop/SqlWithPython/data.db'
conn = sqlite3.connect(database)
c = conn.cursor()

query = """
SELECT * FROM invoices
WHERE BillingCountry = 'Germany' AND Total >= 2.0
"""
c.execute(query)
results = c.fetchall()
for row in results:
    print(row)

c.close()