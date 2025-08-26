import os
from openpyxl import Workbook
import pdfplumber
# Verificar quantos arquivos/pdf existem

diretorio = 'pdf_invoices'
arquivos = os.listdir(diretorio)

qtd_arquivos = len(arquivos)

# Debug
# print(qtd_arquivos)
if qtd_arquivos == 0:
    raise Exception("Nenhum arquivo encontrado na pasta")


# Criando estrutura do arquivo excel


wb = Workbook()
ws = wb.active
ws.title = 'Importacao de Nfs'
# Nomeando as colunas
ws['A1'] = 'Nf #'
ws['B1'] = 'Data'
ws['C1'] = "Nome do Arquivo"
ws['D1'] = 'Status'

ultima_linha_vazia = 1
while ws['A' + str(ultima_linha_vazia)].value is not None:
    ultima_linha_vazia += 1
    

for arquivo in arquivos:
    with pdfplumber.open(diretorio + "/" + arquivo) as pdf:
        primeira_pagina = pdf.pages[0]
        texto_pdf = primeira_pagina.extract_text()
        print(texto_pdf)





