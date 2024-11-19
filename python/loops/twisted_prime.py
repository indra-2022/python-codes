def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
flag1 = 0
if is_prime(n):
    flag1 = 1

rev = 0
temp = n
while temp != 0:
    rev = rev * 10 + temp % 10
    temp //= 10

flag2 = 0
if is_prime(rev):
    flag2 = 1

if flag1 == 1 and flag2 == 1:
    print("Twisted prime number")
else:
    print("Non twisted prime number")
