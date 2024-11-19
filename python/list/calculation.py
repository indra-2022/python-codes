n=int(input("Enter the range--->"))
mylist=[]
sum=0
for i in range(0,n):
    a=int(input("Enter a number: "))
    mylist.append(a)
for i in range(0,n):
    sum=sum+mylist[i]
avg=sum/n
max=max(mylist)
min=min(mylist)
print("Total sum-->",sum)
print("AVG-->",avg)
print("maximum number-->",max)
print("minimum number-->",min)
    

