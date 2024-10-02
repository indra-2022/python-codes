
name = input("Enter the name of the consumer: ")
number = input("Enter the consumer number: ")
month = input("Enter the month: ")
units = float(input("Enter the units consumed: "))
bill_amount = 0
if units <= 100:
    bill_amount = units * 1.80
elif units <= 300:
    bill_amount = (100 * 1.80) + (units - 100) * 2.30
elif units <= 500:
    bill_amount = (100 * 1.80) + (200 * 2.30) + (units - 300) * 2.80
else:
    bill_amount = (100 * 1.80) + (200 * 2.30) + (200 * 2.80) + (units - 500) * 3.50

print("\n Electricity Bill:")
print(f"Consumer Name: {name}")
print(f"Consumer Number: {number}")
print(f"Month: {month}")
print(f"Units Consumed: {units}")
print(f"Total Bill Amount: {bill_amount}")
