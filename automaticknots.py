import numpy as np

def carregar_pontos_de_arquivo(arquivo):
    # Carrega os dados do arquivo de texto
    Q = np.loadtxt(arquivo, delimiter=',')
    return Q

def automaticknots(Q, espaco_entre_knots = 1.0):  
    num_pontos = len(Q)  # Número de pontos (linhas da matriz)
    distancia_total = 0   # Começa em 0 porque ainda não foi percorrida

    # Distância euclidiana entre os pontos
    for i in range(num_pontos - 1):  
        p1, p2 = Q[i], Q[i + 1]  
        distancia_total += np.linalg.norm(p2 - p1)  

    # Calcula o número de nós baseado na distância total
    n = int(distancia_total / espaco_entre_knots)
    
    print("Número de nós calculado:", n)
    return n

# Exemplo de uso da função
arquivo = "C:/Users/henri/OneDrive/Desktop/PiecewiseG1BezierFit-main/scripts/teleop_data.txt"  # Nome do arquivo .txt com os pontos
Q = carregar_pontos_de_arquivo(arquivo)
espaco_entre_knots = 5  # Defina o valor de espaçamento entre knots
n = automaticknots(Q, espaco_entre_knots)
print("Número final de nós:", n)
