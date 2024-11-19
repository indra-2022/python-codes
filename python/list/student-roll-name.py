roll=[]
name=[]
num_students = int(input("Enter the number of students: "))
for i in range(0,num_students):
    r = input("Enter roll number: ")
    n = input("Enter name: ")
    roll.insert(i,r)
    name.insert(i,n)

for i,j in zip(roll,name):
    print(f"{i:<4}{j:<4}")

search_roll = input("Enter a roll number to find the student: ")
for i in range(num_students):
   if roll[i]== search_roll:
       pos=i
       print(roll[i])
       print(name[i])
       break
else:
    print("No student found with roll number",search_roll)

