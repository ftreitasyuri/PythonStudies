from sqlalchemy import create_engine, text
import pandas as pd
import os
from dotenv import load_dotenv
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Carregando env
load_dotenv()


# Recupenrando os valores do .env
ctx = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
    role=os.getenv("SNOWFLAKE_ROLE")
)


# 2. Ler planilha
df = pd.read_csv("checklist_sample.csv")
df["impressao_gerada"] = pd.to_datetime(df["impressao_gerada"], format="%d/%m/%Y %H:%M", errors="coerce")


# 3. Garantir tabela existente
with ctx.cursor() as cur:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS CHECKLIST (
        ARQUIVO STRING,
        IMPRESSAO_GERADA TIMESTAMP_NTZ,
        TITULO STRING
    )
    """)

# Definindo os nomes das colunas como upercase
df.columns = [c.upper() for c in df.columns]


# 4. Carga otimizada com write_pandas
success, nchunks, nrows, _ = write_pandas(
    ctx,
    df,
    table_name="CHECKLIST"
)

print({"success": success, "chunks": nchunks, "rows_loaded": nrows})

ctx.close()