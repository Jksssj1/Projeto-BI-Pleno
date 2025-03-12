import pandas as pd
from os import getenv
from dotenv import load_dotenv
import mysql.connector

load_dotenv()  # Loads from .env

HOST=getenv("HOST")
USER=getenv("USER")
PASSWORD=getenv("PASSWORD")
DATABASE=getenv("DATABASE")
PORT=getenv("PORT")
print(HOST)

"""Create a sample table if it does not exist."""
config = {
    'host': HOST,     # ou seu host do MySQL
    'user': USER,          # seu usuário do MySQL
    'password': PASSWORD, # sua senha do MySQL
    'database': DATABASE,  # nome do banco de dados
    'port':PORT
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()
cursor.execute("select * from fato_sellout")
rows = cursor.fetchall()
print(rows)
for row in rows:
    
    print(row)
    

# Close connection
cursor.close()
connection.close()