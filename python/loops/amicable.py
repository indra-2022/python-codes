n1=int(input("enter first num-->"))
n2=int(input("enter 2nd num-->"))
sum1=0
sum2=0
for i in range(1,n1):
    if n1%i ==0:
        sum1=sum1+i
for i in range(1,n2):
    if n2%i ==0:
        sum2=sum2+i
if sum1==n2 and sum2+n1 :
    print("amicable number")
else:
    print("not a amicable num")
