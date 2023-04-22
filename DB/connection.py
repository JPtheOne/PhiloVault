import pymysql

host = "localhost"
user = "root"
password = "db2022"
database = "docsdb"

connection = pymysql.connect(host = host, user=user, password = password, database=database)
cursor = connection.cursor()

query = "SHOW TABLES"
cursor.execute(query)
tables = cursor.fetchall()

# Fetch and print the content of each table
for table_name in tables:
    table_name = table_name[0]
    print(f"Content of table {table_name}:")

    # Query the data from the table
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    results = cursor.fetchall()

    # Print the content of the table
    for row in results:
        print(row)

    print("\n")  # Add a newline between tables

cursor.close()
connection.close()