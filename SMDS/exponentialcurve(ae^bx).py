#Non Linear Regression
"""
y=ae^bx
Y=logy,A=loga,bloge=B,x=X
Normal Equuations
a=Antilog[A]
b=B/loge
yi=nA+Bxi
xiyi=Axi+Bxi^2

n=5
x=1 5 7 9 12
y=10 15 12 15 21
Estimate 'y' when x=17
ex means x for estimated y
sumx means summation x
sumy means summation of logy
xisq means xi square
esy=estimatted y
"""
import math
n=int(input("enter no.of elements"))
x=list(map(int,input("enter x values").split()))
y=list(map(int,input("enter y values").split()))
ex=int(input("enter x for estimating y"))
sumx=sum(x)
print(sumx)
sumy=0
logy=[]
for i in y:
    logy.append(math.log(i))
    sumy+=math.log(i)
print(sumy)
xilogyi=[]
xisq=0
for i in range(n):
    xilogyi.append(x[i]*logy[i])
    xisq+=x[i]**2
sxilogyi=sum(xilogyi)
print(xisq)
# for finding  A value
Aconstant=((sumy*xisq)-(sxilogyi*sumx))
A1=n*xisq
A2=sumx*sumx
Avalue=(Aconstant/(A1-A2))
print("A value is",Avalue)
# for finding b value
Bconstant=(sumy-sxilogyi)
B1=sumx
B2=xisq
BforA=(Bconstant-((n*Avalue)-(sumx*Avalue)))
Bvalue=(BforA/(B1-B2))
print("B value is:",Bvalue)
a=math.exp(Avalue)
print("a value is:",a)
b=(Bvalue/(0.434))
print("b value is:",b)
#Fitttig into straight line y=ae^bx
e=math.e
p=b*ex
esy=a*(math.pow(e,p))
print("Estimated Y value  is:",esy)




