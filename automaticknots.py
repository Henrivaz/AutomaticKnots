import numpy as np  

def automaticknots(Q, espaco_entre_knots = 1.0):  
    
    num_pontos = Q.shape[0]  # Número de linhas da matriz (quantidade de pontos)
    distancia_total = 0   #começa em 0 pq ainda nao foi percorrida

    # distancia euclidiana entre os pontos
    for i in range(num_pontos - 1):  
        p1, p2 = Q[i], Q[i + 1]  
        distancia_total += np.linalg.norm(p2 - p1)  

    # Calcula o número de nós baseada na distancia
    n = int(distancia_total / espaco_entre_knots)  

    return n  

# Q = np.linspace([0, 0], [10, 0], num=65)    #pega os 65 pontos dentro da distancia definida (exemplo: 10 m)
# espaco_entre_nos = 1.5                     # Espaçamento entre os nós (exemplo: 5 cm)
# n_calculado = automaticknots(Q, espaco_entre_nos)

# print("Número de nós calculado:", n_calculado)
