import win32com.client as win32

def abrir_excel(path, sheet_name, cell, content):
    try:
        excel = win32.Dispatch("Excel.Application")
        excel.Visible = True
        wb = excel.Workbooks.Add()
        sheet = wb.Sheets(1)
        
        # Renomear
        sheet.name = sheet_name
        
        # Conteúdo
        sheet.Range(cell).Value = content
        
        # Salvar
        wb.SaveAs(path)
        
        excel.Quit()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


path = 'exemplo 01.xlsx'
sheet_name = 'ExemploTeste'
cell = 'A1'
content = 'Curso de automação do SAP'

abrir_excel(path, sheet_name, cell, content)