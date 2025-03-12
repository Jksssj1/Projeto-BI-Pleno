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

def create_table(code):
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
    cursor.execute(code)
    connection.commit()
    cursor.close()
    connection.close()

fato_registro_oporotunidade_code = """
        CREATE TABLE IF NOT EXISTS fato_registro_oportunidade (
        id_oportunidade INT AUTO_INCREMENT PRIMARY KEY,
        id_parceiro VARCHAR(100),
        id_produto VARCHAR(100),
        data_registro DATETIME,
        quantidade INT,
        valor_total DECIMAL(10,2), 
        status VARCHAR(100)
        )
    """

fato_sellout_code = """
        CREATE TABLE IF NOT EXISTS fato_sellout (
        id_sellout INT AUTO_INCREMENT PRIMARY KEY,
        id_parceiro VARCHAR(100),  
        id_produto VARCHAR(100),   
        data_fatura DATE,         
        nf VARCHAR(100),           
        quantidade INT,           
        valor_total DECIMAL(10,2) 
    )
    """

create_table(fato_registro_oporotunidade_code)

create_table(fato_sellout_code)
