"""
Paired T-test
n=11
24 17 18 20 19 23 16 18 21 20 19
24 20 22 20 17 24 20 20 18 19 22
los for 5% is 2.58
"""
import math
n=int(input("enter no.of elements "))
x=list(map(int,input("enter x values").split()))
y=list(map(int,input("enter y values").split()))
los=float(input("enter los for 5 %"))
d_sum=[]
sd=0
d=0
for i in range(n):
    d=0
    d=x[i]-y[i]
    d_sum.append(d)
print("sumation of di",sum(d_sum))
d_bar=sum(d_sum)/n
print("d_bar",d_bar)
s=0
s_dsum=0
for i in d_sum:
    s_dsum+=((i-d_bar)**2)
print("summation of di-dbar:",s_dsum)
s=s_dsum/(n-1)
s=math.sqrt(s)
print("s value =",s)
t=(d_bar/(s/math.sqrt(n)))
print("t value is",abs(t),"~","%.2f"%(abs(t)))
if(t<los):
    print("Claim is Valid")
else:
    print("Not Valid")
