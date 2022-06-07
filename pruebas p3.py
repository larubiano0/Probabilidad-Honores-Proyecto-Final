from main import *
import matplotlib.pyplot as plt

n_0 = [4,5,1,7,3]

#P's tomadas usando Numpy Dirichlet distribution

P = [[0,0.37240585, 0.02273727 ,0.49338616, 0.11147072], 
     [0.27647299, 0, 0.05890617, 0.12458766, 0.54003318],
     [0.06716767, 0.06858368, 0, 0.22524363, 0.63900502],
     [0.51885639, 0.31111651, 0.00604218, 0, 0.16398492],
     [0.40543961, 0.23052689, 0.21123723, 0.15279627, 0]]

ts = [] #Valores para t
x_1 = [] #Valores para Q_x1(t)
x_2 = []
x_3 = []
x_4 = []
x_5 = []

betas = [1/8,1/13,1/5,1/3,1/4]

T = 50000

for _ in range(100):

    n, integrales = simulacion(n_0,P,betas,T)

    for t, Q in integrales:

        x_1.append(Q[0])
        x_2.append(Q[1])
        x_3.append(Q[2])
        x_4.append(Q[3])
        x_5.append(Q[4])
        ts.append(t)

    if _%10==0:
        print(_)

k = 0
for xi in [x_1,x_2,x_3,x_4,x_5]:

    plt.title(f'Valor medio de n_{k+1} vs t')
    plt.ylabel(f'Valor medio de n_{k+1}')
    plt.xlabel('t')

    plt.scatter(ts, xi, s = 1)
    plt.savefig(f'{k+1}.jpg')
    plt.clf()
    k+=1
