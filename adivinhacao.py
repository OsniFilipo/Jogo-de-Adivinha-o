import random

import random  # Importa o módulo random para gerar números aleatórios

def jogar_adivinhacao():
    """
    Função principal do jogo de Adivinhação.
    """
    numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100 como o número secreto
    tentativas = 0  # Inicializa o contador de tentativas

    print("Bem-vindo ao jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while True:
        tentativa = int(input("Digite o seu palpite: "))  # Solicita ao jogador que faça um palpite
        tentativas += 1  # Incrementa o contador de tentativas

        if tentativa < numero_secreto:
            print("O número secreto é maior.")  # Informa ao jogador que o número secreto é maior do que o palpite
        elif tentativa > numero_secreto:
            print("O número secreto é menor.")  # Informa ao jogador que o número secreto é menor do que o palpite
        else:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")  # Informa ao jogador que ele acertou o número secreto e quantas tentativas foram necessárias
            break  # Sai do loop enquanto True, encerrando o jogo

def main():
    """
    Função principal do programa.
    """
    jogar_adivinhacao()  # Chama a função jogar_adivinhacao para iniciar o jogo

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa