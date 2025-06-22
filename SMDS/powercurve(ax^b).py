#fit the power curve of the form y=ax^b
#n=5
#x=2 3 4 5 6
#y=8.3 15.4 33.1 65.2 127.4
#estimate y value when x=10
#normal equations 1)nA+Bxisum   2)Axisum+Bxisquare
import math
n=int(input("enter n value:"))
xli=list(map(float,input("enter x values:").split()))
yli=list(map(float,input("enter y values:").split()))
xisum=0
xisquare=0
xlog=0
for i in xli:
    xlog=math.log(i)
    xisum+=xlog
    xisquare+=xlog**2
print("Summation of xi:",xisum)
print("Summation of xi^2:",xisquare)
yisum=0
for i in yli:
    yisum+=math.log(i)
print("Summation of yi: ",yisum)
#logxi*logyi
xiyi=0
for i in range(n):
    xiyi+=math.log(xli[i])*math.log(yli[i])
print("Summmation of xiyi :",xiyi)
Aconstant=((xisquare*yisum)-(xisum*xiyi))
A1=xisquare*n
A2=xisum*xisum
Avalue=(Aconstant/(A1-A2))
Bconstant=(yisum-xiyi)
B1=xisum
B2=xisquare
BforA=(Bconstant-((n*Avalue)-(xisum*Avalue)))
Bvalue=(BforA/(B1-B2))
a=math.exp(Avalue)
print("a value is:",a)
b=Bvalue
print("b value is:",b)
x=float(input("Enter x value for estimatting of y:"))
y=(a*(x**b))
print("By fitting power curve y^=a^+x^b is:",y,"~","%.3f"%y)
