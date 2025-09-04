# Imports
import os
import pandas as pd
from dotenv import load_dotenv
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Carregar variáveis de ambiente
load_dotenv()

# Parâmetros da tabela
TABLE_NAME = 'VENDAS_SMARTTECH'
SCHEMA_NAME = os.getenv("SNOWFLAKE_SCHEMA").upper()
DATABASE_NAME = os.getenv("SNOWFLAKE_DATABASE").upper()

# Carregar dados do Excel
df = pd.read_excel("VENDAS_SMARTTECH.xlsx")

# Conexão com Snowflake usando contexto (fecha automaticamente)
with snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    role=os.getenv("SNOWFLAKE_ROLE"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=DATABASE_NAME,
    schema=SCHEMA_NAME,
) as ctx:

    # Verifica se a tabela existe
    with ctx.cursor() as cur:
        cur.execute(f"""
            SELECT COUNT(*)
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA = '{SCHEMA_NAME}'
              AND TABLE_NAME = '{TABLE_NAME.upper()}'
        """)
        exists = cur.fetchone()[0] > 0

    # Cria a tabela caso não exista
    if not exists:
        print(f"Tabela {TABLE_NAME} não existe. Criando automaticamente...")
        # Definindo tipos básicos, você pode ajustar conforme o DataFrame real
        columns_def = ", ".join([f"{col.upper()} STRING" for col in df.columns])
        create_table_sql = f"CREATE TABLE {TABLE_NAME.upper()} ({columns_def})"
        with ctx.cursor() as cur:
            cur.execute(create_table_sql)
        print(f"Tabela {TABLE_NAME} criada.")

    # Envia os dados para o Snowflake
    print(f"Inserindo dados na tabela {TABLE_NAME}...")
    success, nchunks, nrows, _ = write_pandas(
        conn=ctx,
        df=df,
        table_name=TABLE_NAME.upper()
    )

    print({
        "tabela": TABLE_NAME,
        "success": success,
        "nchunks": nchunks,
        "nrows": nrows
    })
