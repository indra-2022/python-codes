def fun(num,count):
    power=count//2
    div=pow(10,power)
    left=num//div
    right=num%div
    sum=left+right
    
num=int(input("enter a number"))
count=0
dup=num
while num!=0:
    a=num%10
    count+=1
    num=num//10
 fun(dup,count)