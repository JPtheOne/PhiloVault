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
            
    print("-------RETRIEVED DOCS FROM DATABASE -------\n ")
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


def insert_Term(dictionary): #Store temporary terms on database
    connection = pymysql.connect(host = "localhost", user="root", password ="db2022", database="docsdb")
    cursor = connection.cursor()

    cursor.execute("TRUNCATE TABLE term")
    connection.commit()

    for word_id, word in dictionary.items():
        cursor.execute("insert into TERM (id,term) VALUES (%s,%s)ON DUPLICATE KEY UPDATE term = %s", (word_id, word, word))
    connection.commit()

    cursor.close()
    connection.close()