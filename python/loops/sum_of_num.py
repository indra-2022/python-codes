def Sum(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    print(s)

#driver function
num=int(input("Enter a number:"))
Sum(num)