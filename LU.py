import numpy as np


print('\nDECOMPOSIÇÃO LU')
print('')

# DECOMPOSIÇÃO LU
def LU(A):
    n = len(A)
    L = np.eye(n)
    for j in range(n):
        for i in range(j+1,n):
            m = A[i,j]/A[j,j]
            L[i,j]=m
            A[i]=A[i]-m*A[j]
    return(L,A)

# RESOLVENDO TRIANGULAR INFERIOR
def tri_inf(L,b):
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        S = 0
        for j in range(i):
            S = S + L[i,j] * y[j]
        y[i] = (b[i]-S)/L[i,i]
    return y

# RESOLVENDO TRIANGULAR SUPERIOR
def tri_sup(U,b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
            S = 0
            for j in range(i+1,n):
                S = S + U[i,j] * x[j]
            x[i] = (b[i]-S)/U[i,i]
    return x

#MATRIZ DO EXERCÍCIO 2
A = np.array([[4.0, -1, 0, -1, 0, 0], [-1, 4, -1, 0, -1, 0], [0, -1, 4, 0, 0,-1], [-1, 0, 0, 4, -1, 0], [0, -1, 0, -1, 4, -1], [0, 0, -1, 0, -1, 4]])
print("MATRIZ A:")
print(A)

n = len(A)

#B é a matriz identidade
B = np.eye(n)
print('')
print ("MATRIZ B: (IDENTIDADE)")
print(B)
print('')

#Executando a decomposição LU
L, U = LU(A)

#Alocando uma matriz para a inversa
inv = np.zeros((n,n))

#Resolvendo o sistema para achar a inversa e colocando os números na matrix na ordem correta
for i in range(n):
    y = tri_inf(L,B[i])
    x = tri_sup(U,y)
    for j in range (n):
        inv[j][i] = x[j]

#Fomatação dos prints
np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)})

print("MATRIZ L:")
print(L)
print('')

print("MATRIZ U:")
print(U)
print('')

print("MATRIZ A INVERSA:")
print (inv)
print('')