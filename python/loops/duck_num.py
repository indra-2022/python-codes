n=int(input("enter num to check-->"))
dup=n
flag=0
while n !=0:
    r=n%10
    if r == 0:
        flag+=1
    n=n//10
if flag!= 0:
    print(dup,"is a duck num")
else:
    print(dup,"is not a duck number")