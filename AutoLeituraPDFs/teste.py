# -*- coding: utf-8 -*-
import os

# Define o nome da pasta que será lida
diretorio = 'ArquivosChecklists'

# Define o nome do arquivo de saída
nome_arquivo_saida = 'lista_de_arquivos.txt'

try:
    # Verifica se a pasta existe antes de tentar ler
    if not os.path.isdir(diretorio):
        print(f"O diretório '{diretorio}' não foi encontrado.")
        # Cria a pasta se ela não existir
        os.makedirs(diretorio, exist_ok=True)
        print(f"O diretório '{diretorio}' foi criado.")
        # Se a pasta foi criada agora, não há arquivos para listar
        files = []
    else:
        # Pega a lista de arquivos na pasta
        files = os.listdir(diretorio)

    # Abre o arquivo de saída no modo de escrita ('w')
    # O 'with' garante que o arquivo será fechado automaticamente
    with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        # Itera sobre a lista de arquivos
        for file in files:
            # Escreve o nome do arquivo no arquivo de saída, seguido por uma quebra de linha
            arquivo_saida.write(file + '\n')
        
    print(f"A lista de arquivos foi salva com sucesso em '{nome_arquivo_saida}'.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
