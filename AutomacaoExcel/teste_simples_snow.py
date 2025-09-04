import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector

df = pd.DataFrame({"ID": [1, 2, 3], "NOME": ["A", "B", "C"]})

ctx = snowflake.connector.connect(
    user="...",
    password="...",
    account="...",
    warehouse="...",
    database="...",
    schema="...",
    role="..."
)

success, nchunks, nrows, _ = write_pandas(
    conn=ctx,
    df=df,
    table_name="TESTE_PANDAS",
    auto_create_table=True
)

print(success, nchunks, nrows)
ctx.close()
