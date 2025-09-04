import snowflake.connector

conn = snowflake.connector.connect(
    user="smarttechenter",
    password="@IDLbrasil3008",
    account="BBXMUSP-SE74122"
)
print("Conectado!")
conn.close()
