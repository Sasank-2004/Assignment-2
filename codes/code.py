import numpy as np
from  random import randint 
def Determinant(M):
    x = 0
    if len(M)==2:
        return M[0][0]*M[1][1]-M[0][1]*M[1][0]
    else :
        for i in range(len(M)):
            N = np.delete(M,0,axis=0)
            R = np.delete(N,i,axis=1)
            x =x + pow(-1,i)*Determinant(R)*M[0][i] 
        return x
a = randint(0,100)
b = randint(0,100)
c = randint(0,100)
x = randint(0,100)
y = randint(0,100)
z = randint(0,100)
M = np.array([[a,b,c],[a+2*x,b+2*y,c+2*z],[x,y,z]])
print(f'|M| = {Determinant(M)}')
