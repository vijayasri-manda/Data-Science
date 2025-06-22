#Non linear Regression
"""
y=ab^x
logy=y,A=loga,logb=B,x=X
a=antilog(A)
b=antilog(B)

x=0 1 2 3 4 5 6 7
y=10 21 35 59 92 200 400 610
given x for estimatting y is 8
ex means x for estimatting y
sumx means summation of x
xiyi means summation of xiyi
xisq means summation of xi square
logyi means summation of yi square
"""
import math
n=int(input("enter no.of elements"))
x=list(map(int,input("enter x values").split()))
y=list(map(int,input("enter y values").split()))
ex=int(input("enter x ffor estimatting y value"))
sumx=sum(x)
xiyi=0
logyi=0
xisq=0
for i in range(n):
    logyi+=math.log(y[i])
    xiyi+=x[i]*math.log(y[i])
    xisq+=x[i]*x[i]
#for finding Avalue
Aconstant=((xisq*logyi)-(sumx*xiyi))
A1=(n*xisq)
A2=(sumx*sumx)
Avalue=(Aconstant/(A1-A2))
print("A value is:",Avalue)
#for finding Bvalue
Bconstant=(logyi-xiyi)
B1=sumx
B2=xisq
BforA=(Bconstant-((n*Avalue)-(sumx*Avalue)))
Bvalue=(BforA/(B1-B2))
print("Bvalue is:",Bvalue)
a=math.exp(Avalue)
b=math.exp(Bvalue)
esy=a*(math.pow(b,ex))
print("estimatted Y for ab^x is:",esy)
                     
                     
