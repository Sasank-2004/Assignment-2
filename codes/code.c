#include<stdio.h>
#include<stdlib.h>
int main()
{
    int a = rand() , b = rand() , c = rand() , x = rand() , y = rand() , z = rand();
    int M[3][3] = {{a,b,c},{a+2*x,b+2*y,c+2*z},{x,y,z}};
    int det;
    det = M[0][0]*(M[1][1]*M[2][2]-M[2][1]*M[1][2]) - M[0][1]*(M[1][0]*M[2][2]-M[2][0]*M[1][2]) + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]);
    printf("|M| = %d ",det);
}
//7013583615