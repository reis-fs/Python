# coding: utf-8
import random

# meu jogo
meu_jogo = [20, 11, 30, 22, 10, 13]

# variavel para armazenar todos os numeros da megasena através do método construtor list
megasena = list(range(1, 61))

# variavel para saber o numero de testes a realizar
n_teste = int(input("Digite o numero de testes: "))
soma = 0

for i in range(n_teste):
    sorteado = []
    ct = 0

    while meu_jogo != sorteado:
        # criaçao de copia da variavel megasena para não alterar seus valores
        mega_sorteio = megasena.copy()
        sorteado = []

        for j in range(6):  # numero de sorteios
            num_sorteado = random.choice(mega_sorteio)
            sorteado.append(num_sorteado)
            mega_sorteio.remove(num_sorteado)

        # organizar
        sorteado.sort()
        ct += 1

    # variavel para calcular a média
    soma += ct

    print("O resultado do teste %d: %d tentativas" % (i + 1, ct))

soma /= n_teste
print("Média dos resultados:", soma)
