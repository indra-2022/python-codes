n=int(input("enter how many time you want to perform the addition--->"))
sum=0
up=1
a=int(input("enter the value of a-->"))
for i in range(1,n+1):
    sum=sum+(up/pow(a,up+1))
    up=up+3
print(sum)
