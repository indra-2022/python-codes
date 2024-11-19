n=int(input("enter num to check-->"))
dup=n
while n !=0:
    r=n%10
    if r == 0:
         print(dup,"is a duck num")
         break
    n=n//10
if n== 0:
     print(dup,"is not a duck number")
    