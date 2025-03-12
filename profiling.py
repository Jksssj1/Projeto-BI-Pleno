import pandas as pd
from glob import glob
from ydata_profiling import ProfileReport  

registro_oportunidades = r"database/registros_oportunidades.json"
sellout = r"database/sellout.parquet"

# Carregar um dataset 
df_oportunidades = pd.read_json(registro_oportunidades)  
df_sellout = pd.read_parquet(sellout)  

# Criar o relatório de análise exploratória
profile_oportunidades = ProfileReport(df_oportunidades, title="Relatório EDA oportunidades", explorative=True)
profile_sellout = ProfileReport(df_oportunidades, title="Relatório EDA sellout", explorative=True)

# Salvar como HTML

profile_oportunidades.to_file("EDA/relatorio_oportunidades_eda.html")
profile_sellout.to_file("EDA/relatorio_sellout_eda.html")
