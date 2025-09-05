# Função converte qualquer texto para LOWERCASE OU UPPERCASE    

import re

def converte_texto(opc, texto):
    
    # Valida opção        
        if opc == 1:
            try:
                if texto is not None and type(texto) == str: 
                    print("Texto válido!")
                    # converte o texto para UPPERCASE
                    txtUpper = texto.upper()
                    print(f"O texto convertido é: {txtUpper}")
                else:
                    print("Texto Inválido!")
            except Exception as e:
                print(f"Não foi possível analisar o texto: {e}")
        elif opc == 0:
            try:
                if texto is not None and type(texto) == str: 
                    print("Texto válido!")
                    # converte o texto para UPPERCASE
                    txtUpper = texto.lower()
                    print(f"O texto convertido é: {txtUpper}")               
                
                else:
                    print("Texto Inválido!")
            except Exception as e:
                print(f"Não foi possível analisar o texto: {e}")    
        else:
            print("Valor inválido")
            
# continuar = True   

# while continuar is True:
    
#     print("Deseja continuar?\n Sim ou Não")
#     decisao = str(input()).upper()
#     decisao_limpa = re.sub(r'[^\w\s]', '', decisao)
    
#     if decisao_limpa == 'SIM':
                
#         print("#" * 30)        
#         print("Digite o número correspondente à conversão:\n 1 = Sim e 0 = Não")
#         opcao = int(input())         
        
#         print("Digite o texto que deseja converter:")
#         txt = input() 
#         converte_texto(opcao,txt)
        
#     elif decisao_limpa == 'NAO':
#         continuar = False

# print("Programa finalizado!")        