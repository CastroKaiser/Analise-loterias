# Função para calcular fatorial
def fatorial_recursivo(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

# Função de analise combinatoria
def C(n, p):
    return fatorial_recursivo(n) / (fatorial_recursivo(p) * fatorial_recursivo(n - p))

# Função para calculo de combinações de uma sequencia
def CalculoCombinacoes(o):
    resultado = 1
    for i in range(o):
        temp = int(input(f"Digite a {i+1}ª combinação: "))
        resultado *= temp
    print(f"O total de combinações dessa sequência: {resultado}")

# Função para calculo de media
def Media(numero_valores):
    media = 0
    for i in range(numero_valores):
        mediaTemp = float(input(f"Digite o {i+1}º valor: "))
        media += mediaTemp
    media_final = media / numero_valores
    print(f"A média dos valores é: {media_final}")

# Função para pegar os números 
def GetCombination():
    N = int(input("Digite o valor de N: "))
    P = int(input("Digite o valor de P: "))
    operacao = C(N, P)
    print(f"Resultado da combinação C({N},{P}) = {operacao}")

# Função para pegar os números a serem combinados
def GetCalc():
    value = int(input("Quantas combinações deseja calcular: "))
    CalculoCombinacoes(value)

# Programa principal
escolha = -1

while escolha != 0:
    print("\n=== Menu de Opções ===")
    print("1 - Cálculo de combinação C(n, p)")
    print("2 - Multiplicação de várias combinações")
    print("3 - Cálculo de média")
    print("0 - Sair")
    
    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if escolha == 1:
        GetCombination()
    elif escolha == 2:
        GetCalc()
    elif escolha == 3:
        qtdValores = int(input("Digite a quantidade de números que deseja tirar a média: "))
        Media(qtdValores)
    elif escolha == 0:
        print("Tchau!")
    else:
        print("Opção inválida. Tente novamente.")

