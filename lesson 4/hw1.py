n=int(input("Enter a number:"))
x=str(n)
length = len(x)
total=0
for i in x:
    
    total += int(i)**3
print(f"The sum of the cubes of the digits of {n} is: {total}")
