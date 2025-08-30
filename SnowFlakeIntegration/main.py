from sqlalchemy import create_engine
import pandas as pd

# 1. Ler planilha
df = pd.read_excel("resultados.xlsx")

# 2. Conectar com SQLAlchemy
engine = create_engine(
    'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}'.format(
        user="SEU_USUARIO",
        password="SUA_SENHA",
        account="SEU_ACCOUNT_ID",
        database="SEU_DATABASE",
        schema="SEU_SCHEMA",
        warehouse="SEU_WAREHOUSE"
    )
)

# 3. Enviar dataframe
df.to_sql('checklist', engine, if_exists='append', index=False)
