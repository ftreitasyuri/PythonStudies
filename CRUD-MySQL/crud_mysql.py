import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='laravel-vue-inertia'
)
# laravel-vue-inertia

cursor = conexao.cursor()

# INICIO CRUD

nome = "Marcos Paulo2"
email = "mpaulo2@teste.com"
telefone = "11940028922"
# CREATE
comando = f'INSERT INTO clients (nome_cliente, email_cliente, telefone_cliente) VALUES ("{nome}", "{email}", "{telefone}")'

# Para executar a query
cursor.execute(comando)

# Para popular os dados no banco
conexao.commit()

# FIM CRUD

cursor.close()
conexao.close()