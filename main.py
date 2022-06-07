from numpy import random

def simulacion(n, P, betas, T):
    """
    n = Q_0, es la configuración de la red
    en el instante 0, tiene estructura
    de lista de Python. A medida que toma
    lugar la simulación, n va cambiando

    P, matriz cuya entrada ij representa
    la probabilidad de que al salir un cliente 
    del nodo i, vaya al nodo j. Estructura 
    de lista de listas de Python.

    betas, son el parametro del tiempo de
    servicio para un nodo j, que toma
    distribución exponencial(b_j)

    T, tiempo final hasta el que se va a
    realizar la simulación. Esta inicia
    en el tiempo t = 0. int de Python

    Retorna: n final, integrales --> tupla (t,Q(t))
    """

    k = len(n) #Número de nodos
    m = sum(n) #Número total de clientes

    assert len(P)==k, "Tamaño de la matriz no coincide con k"
    assert len(P[0])==k, "Tamaño de la matriz no coincide con k" #Verifica que dim(P)=kxk

    assert len(betas)==k, "Tamaño de betas no coincide con k" #Verifica que dim(betas) = k

    assert type(T) == int, "T no es un entero" #Verifica que T sea un entero positivo
    assert T>=0, "T es negativo"

    for i in P: #Verifica que las filas de P sumen 1

        assert sum(i) == 1, "Las filas de P no suman 1"



    esperas = [float('inf') for i in range(k)] #Crea lista con tiempos de espera para las personas en cada nodo
    
    suma = [0] * k #Suma Q para cada tiempo

    valores_integral = [] #Valores que toma la integral, lista de tuplas de tipo (t,Q(t))


    for t in range(T):
        
        for i in range(k): 


            if esperas[i] != float('inf') and n[i]>0: #Si hay tiempo de espera lo disminuye en 1 

                esperas[i] = esperas[i] - 1 

            elif esperas[i] == float('inf') and n[i]>0: #Si no hay tiempo de espera y hay personas, inicia el tiempo de espera

                esperas[i] = random.exponential(1/betas[i]) #Toma como parametro el inverso de beta


            if esperas[i]<=0 and n[i]>0: #Si se acabó el tiempo de espera

                n[i] = n[i] - 1 #Disminuye en 1 la cantidad de personas en i

                probabilidades = P[i]

                j = random.choice([j for j in range(k)], p=probabilidades) #Selecciona el nodo j para enviar a la persona
                
                n[j] = n[j] + 1 #Aumenta en 1 la cantidad de personas en j

                esperas[i] = float('inf') #Pone en infinito el tiempo de espera para el nodo i
        

        suma = [x + y for x, y in zip(suma, n)] #Agrega a la suma el número de personas en n para t.

        if t !=0: #evita división por 0

            integral = [i/t for i in suma] #Calcula la integral del Teorema Ergódico, divide por T la suma.

            valores_integral.append((t, integral))

    return n, valores_integral