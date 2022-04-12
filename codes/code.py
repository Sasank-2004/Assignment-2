import numpy as np
from  random import randint 
a = randint(0,100)
b = randint(0,100)
c = randint(0,100)
x = randint(0,100)
y = randint(0,100)
z = randint(0,100)
M = np.array([[a,b,c],[a+2*x,b+2*y,c+2*z],[x,y,z]])
det = np.linalg.det(M)
print(f'|M| = {det}')
