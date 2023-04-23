import pymysql

#Credentials
host = "localhost"
user = "root"
password = "db2022"
database = "docsdb"

def get_docContent():
    connection = pymysql.connect(host = host, user=user, password = password, database=database)
    cursor = connection.cursor()

    #Retrieving text
    query = "Select id, language, content from document"
    cursor.execute(query)
    results = cursor.fetchall()
    
    for result in results:
        id, language, text = result
        print(f"Doc{id}:")
        print(f"Language: {language}")
        print(f"Text: {text}")
        print()
   
    
    #Closing database
    cursor.close()
    connection.close()

get_docContent()