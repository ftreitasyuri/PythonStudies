# print('Hello world!')

import mysql.connector

# Conectando com o banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="laravel-vue-inertia"

)

cursor = conn.cursor()

# Consulta simples
cursor.execute("SELECT * FROM clients")

# Exibindo os resultados
for row in cursor.fetchall():
    print(row)

# Fechando conexão
cursor.close()
conn.close()