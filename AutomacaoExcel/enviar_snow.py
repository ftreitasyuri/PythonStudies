# Função para enviar os dados tratados para o snowFlake

# Imports
import os
import pandas as pd
from dotenv import load_dotenv
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Carregar dotEnv
load_dotenv()


# Pega as variáveis de ambiente
ctx = snowflake.connector.connect(
    user = os.getenv("SNOWFLAKE_USER"),
    password = os.getenv("SNOWFLAKE_PASSWORD"),
    account = os.getenv("SNOWFLAKE_ACCOUNT"),
    role = os.getenv("SNOWFLAKE_ROLE"),
    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE"),
    database = os.getenv("SNOWFLAKE_DATABASE"),
    schema = os.getenv("SNOWFLAKE_SCHEMA"),
)
# Escapar senha
# encoded_password = quote_plus(ctx.password)

df = pd.read_excel("VENDAS_SMARTTECH.xlsx")


table_name = 'VENDAS_SMARTTECH'

# Verifica se a tabela já existe no snowFlake
with ctx.cursor() as cur:
    cur.execute(f"""
                SELECT COUNT(*)
                FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_SCHEMA = '{os.getenv("SNOWFLAKE_SCHEMA")}'
                AND TABLE_NAME = '{table_name}'
                """)
    exists = cur.fetchone()[0] > 0

if not exists:
    print(f"Tabela {table_name} não existe. Criando automaticamente...")
    success, nchunks, nrows, _ = write_pandas(
        conn=ctx,
        df=df,
        table_name=table_name
        
    )
else:
    print(f"Tabela {table_name} já existe, Inserindo dados...")
    success, nchunks, nrows, _ = write_pandas(
        conn=ctx,
        df=df,
        table_name=table_name
    )

print({
    "tabela": table_name,
    "success": success,
    "nchunks": nchunks,
    "nrows": nrows
})


ctx.close()