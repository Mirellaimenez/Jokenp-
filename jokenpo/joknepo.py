import random

escolhas = ["pedra", "papel", "tesoura"]
jogada = input("Escolha pedra, papel ou tesoura: ")
computer_choice = random.choice(escolhas)
print("O computador escolheu", computer_choice)

# comparar as escolhas e imprimir o resultado
if jogada == computer_choice:
    print("Empate!")
elif jogada == "pedra" and computer_choice == "tesoura" or \
       jogada== "papel" and computer_choice == "pedra" or \
       jogada == "tesoura" and computer_choice == "papel":
    print("Você ganhou!")
else:
    print("Você perdeu!")

