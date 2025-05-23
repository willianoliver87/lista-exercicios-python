                     #Exercícios-Prof Júlio

# EXERCÍCIOS 31 A 38: MATRIZES

# 31. Soma de partes de uma matriz 5x5
M = [[int(input(f"M[{i}][{j}]: ")) for j in range(5)] for i in range(5)]

print("Soma da linha 3:", sum(M[2]))
print("Soma da coluna 2:", sum([M[i][1] for i in range(5)]))
print("Soma diagonal principal:", sum([M[i][i] for i in range(5)]))
print("Soma diagonal secundária:", sum([M[i][4-i] for i in range(5)]))
print("Soma total:", sum([sum(linha) for linha in M]))

# 32. Soma e diferença de duas matrizes 4x6
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(6)] for i in range(4)]
B = [[int(input(f"B[{i}][{j}]: ")) for j in range(6)] for i in range(4)]

S = [[A[i][j] + B[i][j] for j in range(6)] for i in range(4)]
D = [[A[i][j] - B[i][j] for j in range(6)] for i in range(4)]

print("Matriz Soma:")
for linha in S:
    print(linha)

print("Matriz Diferença:")
for linha in D:
    print(linha)

# 33. Somar regiões específicas em matriz 4x4
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(4)] for i in range(4)]
print("Soma quadrante superior esquerdo:", A[0][0] + A[0][1] + A[1][0] + A[1][1])
print("Soma inferior direito:", A[2][2] + A[2][3] + A[3][2] + A[3][3])
print("Soma triangular inferior:", sum([A[i][j] for i in range(4) for j in range(i+1)]))
print("Soma triangular superior:", sum([A[i][j] for i in range(4) for j in range(i, 4)]))

# 34. Verifica se número existe na matriz
D = [[int(input(f"D[{i}][{j}]: ")) for j in range(5)] for i in range(5)]
X = int(input("Digite o valor a procurar: "))
existe = any(X == D[i][j] for i in range(5) for j in range(5))
print("Existe na matriz." if existe else "Não existe na matriz.")

# 35. Soma das linhas e colunas da matriz 5x5
G = [[int(input(f"G[{i}][{j}]: ")) for j in range(5)] for i in range(5)]
SL = [sum(G[i]) for i in range(5)]
SC = [sum(G[i][j] for i in range(5)) for j in range(5)]
print("Soma das linhas:", SL)
print("Soma das colunas:", SC)

# 36. Divide cada linha pelo maior valor da linha
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(13)] for i in range(12)]
for i in range(12):
    maior = max(A[i])
    A[i] = [x / maior for x in A[i]]
print("Matriz normalizada:")
for linha in A:
    print(linha)

# 37 e 38. Gabarito de loteria e comparação com aposta
gabarito = [int(input(f"Gabarito {i+1} (1-3): ")) for i in range(13)]
aposta = [[int(input(f"Aposta [{i}][{j}] (1 ou 0): ")) for j in range(3)] for i in range(13)]

pontos = 0
simples = dupla = tripla = 0

for i in range(13):
    tipo = sum(aposta[i])
    if tipo == 1:
        simples += 1
    elif tipo == 2:
        dupla += 1
    elif tipo == 3:
        tripla += 1
    if aposta[i][gabarito[i]-1] == 1:
        pontos += 1

print("Pontos:", pontos)
print("Simples:", simples, "Dupla:", dupla, "Tripla:", tripla)

# EXERCÍCIOS 39 A 45: FUNÇÕES

# 39. Calculadora com funções
def calculadora(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else "Erro: divisão por zero"
    else:
        return "Operação inválida"

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
op = input("Digite a operação (+ - * /): ")
print("Resultado:", calculadora(a, b, op))

# 40. Multiplicação por somas
def mult_por_soma(a, b):
    total = 0
    for _ in range(int(b)):
        total += a
    return total

print("Multiplicação (por soma):", mult_por_soma(a, b))

# 41. Velocidade média
def velocidade_media(dist, tempo):
    return dist / tempo

dist = float(input("Distância (m): "))
tempo = float(input("Tempo (s): "))
print("Velocidade média:", velocidade_media(dist, tempo), "m/s")

# 42. Versão com função divisão
def divisao(a, b):
    return a / b if b != 0 else 0

def velocidade_media_2(dist, tempo):
    return divisao(dist, tempo)

print("Velocidade média (função interna):", velocidade_media_2(dist, tempo), "m/s")

# 43. Organização de número
def organiza(numero):
    texto = str(numero)
    crescente = "".join(sorted(texto))
    decrescente = "".join(sorted(texto, reverse=True))
    reverso = texto[::-1]
    return crescente, decrescente, reverso

num = int(input("Digite um número: "))
c, d, r = organiza(num)
print("Crescente:", c)
print("Decrescente:", d)
print("Reverso:", r)

# 44. Conversor 24h para 12h
def converter_hora(h, m):
    periodo = 'A' if h < 12 else 'P'
    h12 = h % 12
    if h12 == 0:
        h12 = 12
    return h12, m, periodo

while True:
    h = int(input("Hora (0-23): "))
    m = int(input("Minuto (0-59): "))
    h12, m12, p = converter_hora(h, m)
    print(f"{h12}:{m12:02d} {'A.M.' if p == 'A' else 'P.M.'}")
    if input("Deseja continuar? (s/n): ").lower() != 's':
        break

# 45. Data por extenso
def mes_extenso(mes):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    return meses[mes-1] if 1 <= mes <= 12 else None

def data_por_extenso(data):
    try:
        d, m, a = map(int, data.split("/"))
        mes = mes_extenso(m)
        if mes:
            return f"{d} de {mes} de {a}"
        else:
            return "NULL"
    except:
        return "NULL"

data = input("Digite a data (DD/MM/AAAA): ")
print("Data por extenso:", data_por_extenso(data))
