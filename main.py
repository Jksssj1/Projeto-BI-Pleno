import pandas as pd
from os import getenv
from dotenv import load_dotenv
import mysql.connector
import hashlib
from sqlalchemy import create_engine

load_dotenv()  # Loads from .env

HOST=getenv("HOST")
USER=getenv("USER")
PASSWORD=getenv("PASSWORD")
DATABASE=getenv("DATABASE")
PORT=getenv("PORT")

engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

registro_oportunidades = r"database/registros_oportunidades.json"
sellout = r"database/sellout.parquet"

df_oportunidades = pd.read_json(registro_oportunidades) 
df_sellout = pd.read_parquet(sellout)  

df_oportunidades['id_parceiro'] = df_oportunidades['CNPJ Parceiro'].apply(lambda x: hashlib.md5(x.encode()).hexdigest())
df_oportunidades['id_produto'] = df_oportunidades['Nome_Produto'].apply(lambda x: hashlib.md5(x.encode()).hexdigest())
df_oportunidades['data_registro'] = pd.to_datetime(df_oportunidades['Data de Registro'],unit='ms')
df_oportunidades['quantidade'] = df_oportunidades['Quantidade']
df_oportunidades['valor_total'] = df_oportunidades['Valor_Unitario']*df_oportunidades['Quantidade']
df_oportunidades['status'] = df_oportunidades['Status']

df_oportunidades_final = df_oportunidades[['id_parceiro','id_produto','data_registro','quantidade','valor_total','status']]

df_sellout['id_parceiro'] = df_sellout['CNpj Parceiro'].apply(lambda x: hashlib.md5(x.encode()).hexdigest())
df_sellout['id_produto'] = df_sellout['Nome_Produto'].apply(lambda x: hashlib.md5(x.encode()).hexdigest())
df_sellout['data_fatura'] = pd.to_datetime(df_sellout['Data_Fatura'],unit='ms')
df_sellout['nf'] = df_sellout['NF']
df_sellout['quantidade'] = df_sellout['Quantidade']
df_sellout['valor_total'] = df_sellout['Valor_Unitario']*df_sellout['Quantidade']

df_sellout_final = df_sellout[['id_parceiro','id_produto','data_fatura','nf','quantidade','valor_total']]

df_sellout_final.to_excel('fato_sellout_final.xlsx')
 
df_oportunidades_final.to_excel('fato_oportunidades_final.xlsx')
 
"""
df_sellout_final.to_sql(
    name="fato_sellout",    # Table name in MySQL
    con=engine,             # Connection engine
    if_exists="append",     # Options: "fail", "replace", "append"
    index=False             # Do not write the index as a column
)
df_oportunidades_final.to_sql(
    name="fato_registro_oportunidade",
    con=engine,
    if_exists="append",
    index=False
)"""



