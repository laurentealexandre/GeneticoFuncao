import random
import math

# Função para obter input do usuário com validação
def obter_input_valido(mensagem, tipo, min_valor=None, max_valor=None):
    while True:
        try:
            valor = tipo(input(mensagem))
            if min_valor is not None and valor < min_valor:
                raise ValueError
            if max_valor is not None and valor > max_valor:
                raise ValueError
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")

# Configurações por input do usuário
TAMANHO_POPULACAO = obter_input_valido("Digite o tamanho da população inicial: ", int, 1)
TAXA_MUTACAO = obter_input_valido("Digite a taxa de mutação (entre 0 e 1): ", float, 0, 1)
PONTOS_CRUZAMENTO = obter_input_valido("Digite o número de pontos de cruzamento (1 ou 2): ", int, 1, 2)

# Outras configurações (podem ser transformadas em input se necessário)
TAMANHO_TORNEIO = 3
USAR_ELITISMO = True
PERCENTUAL_ELITISMO = 0.1
MAX_GERACOES = 100
TAMANHO_CROMOSSOMO = 16  # Tamanho do cromossomo binário

# Função objetivo
def funcao_objetivo(x):
    return x**3 - 6*x + 14

# Decodificar binário para decimal
def decodificar_cromossomo(cromossomo):
    decimal = int(''.join(map(str, cromossomo)), 2)
    return -10 + decimal * (20 / (2**TAMANHO_CROMOSSOMO - 1))

# Criar indivíduo aleatório
def criar_individuo():
    return [random.randint(0, 1) for _ in range(TAMANHO_CROMOSSOMO)]

# Criar população inicial
def criar_populacao_inicial():
    return [criar_individuo() for _ in range(TAMANHO_POPULACAO)]

# Calcular aptidão
def calcular_aptidao(individuo):
    x = decodificar_cromossomo(individuo)
    return 1 / (1 + abs(funcao_objetivo(x)))  # Minimização

# Seleção por torneio
def selecao_torneio(populacao):
    torneio = random.sample(populacao, TAMANHO_TORNEIO)
    return max(torneio, key=calcular_aptidao)

# Cruzamento
def cruzamento(pai1, pai2):
    if PONTOS_CRUZAMENTO == 1:
        ponto = random.randint(1, TAMANHO_CROMOSSOMO - 1)
        filho1 = pai1[:ponto] + pai2[ponto:]
        filho2 = pai2[:ponto] + pai1[ponto:]
    else:  # 2 pontos
        ponto1, ponto2 = sorted(random.sample(range(1, TAMANHO_CROMOSSOMO), 2))
        filho1 = pai1[:ponto1] + pai2[ponto1:ponto2] + pai1[ponto2:]
        filho2 = pai2[:ponto1] + pai1[ponto1:ponto2] + pai2[ponto2:]
    return filho1, filho2

# Mutação
def mutacao(individuo):
    return [1 - gene if random.random() < TAXA_MUTACAO else gene for gene in individuo]

# Algoritmo genético principal
def algoritmo_genetico():
    populacao = criar_populacao_inicial()
    
    for geracao in range(MAX_GERACOES):
        populacao = sorted(populacao, key=calcular_aptidao, reverse=True)
        
        nova_populacao = []
        tamanho_elite = int(TAMANHO_POPULACAO * PERCENTUAL_ELITISMO) if USAR_ELITISMO else 0
        nova_populacao.extend(populacao[:tamanho_elite])
        
        while len(nova_populacao) < TAMANHO_POPULACAO:
            pai1 = selecao_torneio(populacao)
            pai2 = selecao_torneio(populacao)
            filho1, filho2 = cruzamento(pai1, pai2)
            nova_populacao.extend([mutacao(filho1), mutacao(filho2)])
        
        populacao = nova_populacao[:TAMANHO_POPULACAO]
        
        melhor_individuo = max(populacao, key=calcular_aptidao)
        melhor_x = decodificar_cromossomo(melhor_individuo)
        melhor_y = funcao_objetivo(melhor_x)
        
        print(f"Geração {geracao + 1}: x = {melhor_x:.4f}, f(x) = {melhor_y:.4f}")
    
    return melhor_x, melhor_y

# Executar o algoritmo
print("Configurações do Algoritmo Genético:")
print(f"Tamanho da população: {TAMANHO_POPULACAO}")
print(f"Taxa de mutação: {TAXA_MUTACAO}")
print(f"Pontos de cruzamento: {PONTOS_CRUZAMENTO}")
print("\nIniciando o algoritmo genético...\n")

melhor_x, melhor_y = algoritmo_genetico()
print(f"\nMelhor solução encontrada:")
print(f"x = {melhor_x:.4f}")
print(f"f(x) = {melhor_y:.4f}")