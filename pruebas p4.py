from main import *
import matplotlib.pyplot as plt
import numpy as np


#P's tomadas usando Numpy Dirichlet distribution

P = [[0,0.37240585, 0.02273727 ,0.49338616, 0.11147072], 
     [0.27647299, 0, 0.05890617, 0.12458766, 0.54003318],
     [0.06716767, 0.06858368, 0, 0.22524363, 0.63900502],
     [0.51885639, 0.31111651, 0.00604218, 0, 0.16398492],
     [0.40543961, 0.23052689, 0.21123723, 0.15279627, 0]]

m50 = [] #Valores para m = 50
m100 = [] 
m200 = []

betas = [1/8,1/13,1/5,1/3,1/4]

T = 100000

n_0m = zip(([8,2,20,11,9], [16,4,40,22,18], [32,8,80,44,36]), [m50,m100,m200])

for n_0, m in n_0m:

    for _ in range(100):

        n, integrales = simulacion(n_0,P,betas,T)

        m.append(integrales[-1][1]) #Solo el valor

        if _%10==0:
            print(_)

m50x1 = sum(i[0] for i in m50)/len(m50) #Promedios para cada x
m50x2 = sum(i[1] for i in m50)/len(m50)
m50x3 = sum(i[2] for i in m50)/len(m50)
m50x4 = sum(i[3] for i in m50)/len(m50)
m50x5 = sum(i[4] for i in m50)/len(m50)

m100x1 = sum(i[0] for i in m100)/len(m100) 
m100x2 = sum(i[1] for i in m100)/len(m100)
m100x3 = sum(i[2] for i in m100)/len(m100)
m100x4 = sum(i[3] for i in m100)/len(m100)
m100x5 = sum(i[4] for i in m100)/len(m100)

m200x1 = sum(i[0] for i in m200)/len(m200) 
m200x2 = sum(i[1] for i in m200)/len(m200)
m200x3 = sum(i[2] for i in m200)/len(m200)
m200x4 = sum(i[3] for i in m200)/len(m200)
m200x5 = sum(i[4] for i in m200)/len(m200)

x = np.array([50,100,200])

################################################################
plt.title('Limite del valor medio de n_1 vs m')
plt.ylabel('Limite del valor medio de n_1')
plt.xlabel('m')
plt.scatter(x, [m50x1,m100x1,m200x1], s = 10)

a, b = np.polyfit(x, [m50x1,m100x1,m200x1], 1)
plt.plot(x, a*x + b)

print(a,b)

plt.savefig('limitesx1.jpg')
plt.clf()
################################################################
plt.title('Limite del valor medio de n_2 vs m')
plt.ylabel('Limite del valor medio de n_2')
plt.xlabel('m')
plt.scatter(x, [m50x2,m100x2,m200x2], s = 10)

a, b = np.polyfit(x, [m50x2,m100x2,m200x2], 1)
plt.plot(x, a*x + b)

print(a,b)

plt.savefig('limitesx2.jpg')
plt.clf()
################################################################
plt.title('Limite del valor medio de n_3 vs m')
plt.ylabel('Limite del valor medio de n_3')
plt.xlabel('m')
plt.scatter(x, [m50x3,m100x3,m200x3], s = 10)

a, b = np.polyfit(x, [m50x3,m100x3,m200x3], 1)
plt.plot(x, a*x + b)

print(a,b)

plt.savefig('limitesx3.jpg')
plt.clf()
################################################################
plt.title('Limite del valor medio de n_4 vs m')
plt.ylabel('Limite del valor medio de n_4')
plt.xlabel('m')
plt.scatter(x, [m50x4,m100x4,m200x4], s = 10)

a, b = np.polyfit(x, [m50x4,m100x4,m200x4], 1)
plt.plot(x, a*x + b)

print(a,b)

plt.savefig('limitesx4.jpg')
plt.clf()
################################################################
plt.title('Limite del valor medio de n_5 vs m')
plt.ylabel('Limite del valor medio de n_5')
plt.xlabel('m')
plt.scatter(x, [m50x5,m100x5,m200x5], s = 10)

a, b = np.polyfit(x, [m50x5,m100x5,m200x5], 1)
plt.plot(x, a*x + b)

print(a,b)

plt.savefig('limitesx5.jpg')
plt.clf()