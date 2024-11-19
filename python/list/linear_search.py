n=int(input("Enter the range--->"))
mylist=[]
pos=[]
flag=0
for i in range(0,n):
    a=int(input("Enter a number: "))
    mylist.append(a)
a=int(input("enter the number to search-->"))
for i in range(0,n):
    if mylist[i]==a:
        flag=1
        pos.append(i)
if flag>0 :
    print("The element"+str(a)+" was found at index "+str(pos))

