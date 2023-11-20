num1 = float(input("Enter The First number: "))
num2 = float(input("Enter the second number: "))
i = 1
while(i <= num1 and i<= num2):
    if(num1 % i == 0 and num2 %i ==0):
        gcd = i
        i = i+1
        print(f"gcd is{gcd}")
print(f"gcd is {gcd}")
