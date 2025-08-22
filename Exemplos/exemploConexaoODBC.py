# Importanto bibliotecas
import pyodbc

# Conexão com o banco
server = 'IPDOSERVIDOR'
database = 'NOMEBANCODEDADOS'
username = 'NOMEUSER'
password = 'SENHADOUSUARIO'

# String de conexao

connection_string = (
    #"DRIVER={{ODBC Driver 17 fro SQL Server}};"    
    "DRIVER={ODBC Driver 18 for SQL Server};"  
    # f"SERVER=(server),{1433};"
    f"SERVER={server},1433;"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=no;"  # Desativa criptografia
    "TrustServerCertificate=yes;"  # Ignora certificado inválido
    
)


# Tentativa de conexão
try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
    cpf_unico = '16132169717'
    # Select simples
    # cursor.execute("SELECT TOP 10 * FROM usu_tcadfun")
    cursor.execute("SELECT TOP 2 * FROM usu_tcadfun WHERE usu_cpf = ? ", (cpf_unico))
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
except Exception as e:
    print("Erro na conexão", e)
finally:
    if 'conn' in locals():
        conn.close()