n=int(input("enter num to convert"))
p=0
dec=0
while n !=0:
    r=n%10
    dec=dec+r*pow(2,p)
    n=n//10
    p+=1
print("decimal -->",dec)

