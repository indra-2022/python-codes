sum=0
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("enter N-->"))
m=int(input("enter M-->"))
x=n-m
nfact=factorial(n)
mfact=factorial(m)
xfact=factorial(x)
sum=nfact/(mfact*xfact)
print(sum)


