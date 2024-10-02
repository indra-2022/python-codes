def fibo(n):
    a = 0
    b = 1
    print(a, b, end=", ")
    for i in range(3, n + 1):
        s = a + b 
        print(s, end=" ")
        a = b 
        b = s  
num = int(input("Enter the number of terms: "))
fibo(num)
