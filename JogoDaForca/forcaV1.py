# Importando bibliotecas
import random
from os import system, name


# Função para limpar a tela a cada execução
def limpa_tela():
    
    #Windows
    if name == 'nt':
        _ = system('cls')
    # MAC E LINUX
    else:
        _ = system('clear')


# Função game
def game():
    
    limpa_tela()
    print("\nBem-vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
        
    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolhendo randomicamente uma palavra
    palavra = random.choice(palavras)
    
    # List comprehension => retornando um - para cada letra na palavra selecionada
    letras_descobertas = ['_' for letra in palavra]
    
    print(letras_descobertas)
    
    # Número de chances
    chances = 6
    
    # Lista para as letras erradas
    letras_erradas = []
    
    # Loop enquanto número de chances for maior do que zero
    while chances > 0:
        
        #Print
        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas:", "".join(letras_erradas))
        
        #Tentativa
        tentativa = input("\nDigite uma letra: ").lower()
    
        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index +=1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
        # Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
        
        
    
game()