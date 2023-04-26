import pymysql

#Credentials
host = "localhost"
user = "root"
password = "db2022"
database = "docsdb"

def get_docContent(language): #Retrieve the texts from documents with given language
    connection = pymysql.connect(host = host, user=user, password = password, database=database)
    cursor = connection.cursor()

    #Retrieving text
    query = f"Select id, title, author, content from DOCUMENT where language ='{language}';"
    cursor.execute(query)
    results = cursor.fetchall()
    
    docs = []
    for result in results:
        id, title, author, content = result
        docs.append(content)

        print(f"Doc{id}")
        print(f"Title: {title}")
        print(f"Author: {author}")
        print()
   
    #Closing database
    cursor.close()
    connection.close()

    return docs


def insert_Term():
    pass