def odd_even(n):
     for i in range(1,n+1):
          if(i%2==0):
               print(i,"even number")
          else:
               print(i,"odd number")
              
num=int(input("enter num-->"))
odd_even(num)

