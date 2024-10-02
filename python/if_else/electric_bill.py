
name = input("Enter the name of the consumer: ")
number = input("Enter the consumer number: ")
month = input("Enter the month: ")
units = float(input("Enter the units consumed: "))
if units <= 100:
    charge = 1.80
elif units <= 300:
    charge = 2.30
elif units <= 500:
    charge = 2.80
else:
    charge = 3.50
bill = units * charge
print("\nBill Details")
print(f"Consumer Name: {name}")
print(f"Consumer Number: {number}")
print(f"Month: {month}")
print(f"Units Consumed: {units}")
print(f"Charge per Unit: {charge}")
print(f"Total Bill Amount: {bill}")
