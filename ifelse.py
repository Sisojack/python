mark=int(input("Enter Marks: "))
if 80 <= mark <= 100:
    print("You have an A")
elif mark >=60 and mark<=79:
    print("You have a B")
elif mark >=40 and mark<=59:
    print("You have a B")
elif mark >=0 and mark<=39:
    print("You are a failure!!")
else:
    print("Wrong inputs")
num1=int(input("Enter Number: "))
num2=int(input("Enter Number: "))
num3=int(input("Enter Number: "))
num4=int(input("Enter Number: "))
if num1>num2 and num1>num3 and num1>num4:
    print(f"The largest number is {num1}")
elif num2>num1 and num2>num3 and num2>num4:
    print(f"The largest number is {num2}")
elif num3>num2 and num3>num4 and num3>num1:
    print(f"The largest number is {num3}")
elif num4>num3 and num4>num2 and num4>num1:
    print(f"The largest number is {num4}")
else:
    print("No number is greater")