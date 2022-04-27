import numpy as np
#Метод прогонки

B=np.array([[1,1.12,0,0,0,7.94],[1.12,4.28-1.5,2.12,0,0,3.21],[0,2.12,6.13+1.5,1.29,0,4.28-1.75],[0,0,1.29,4.57-1.5,1.25,6.25],[0,0,0,1.25,5.21+1.5,4.95+1.75]])
#B=np.array([[8., 1., -4., 6.], [2., -6., 1., -9.], [-1., 1., 4., 5.]])
#Рахуємо коефіцієнти для методу прогонки
Acof,Bcof,Sol=[],[],[]
Acof.append(-B[0][1]/B[0][0])#A1
Bcof.append(B[0][5]/B[0][0])#B1
for i in range(1,4):
    Acof.append(-B[i][i+1]/(B[i][i]+B[i][i-1]*Acof[i-1]))
for i in range(1,5):
    Bcof.append((B[i][5]-B[i][i-1]*Bcof[i-1])/(B[i][i]+B[i][i-1]*Acof[i-1]))
Acof.append(0.0)
Sol.append(Bcof[4])
#Підставляємо отримані коефіцієнти в рівняння і знаходимо розвязок
for i in range(3,-1,-1):
    a=Sol.pop()
    Sol.append(a)
    Sol.append(Acof[i]*a+Bcof[i])
Sol.reverse()
print(Acof)
print(Bcof)
print(Sol)