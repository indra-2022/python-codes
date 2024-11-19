n=int(input("enter num to check-->"))
flag=0
for i in range(1,n+1):
    if n//i==0:
        flag+=1
if flag==2:
    print(n,"is a pronic num")
else:
    print(n,"is not a pronic num")
