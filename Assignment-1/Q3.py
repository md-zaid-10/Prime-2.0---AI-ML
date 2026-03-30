# Ask the user to enter two integers and one float.Convert them all to floats and print their average

print("Please enter two numbers: ")

num1 = int((input("Enter First number in integer: ")))
num2 = int((input("Enter Second number in integer: ")))
num3 = float((input("Enter Third number in float: ")))

num1 = float(num1)
num2 = float(num2)

average = (num1 + num2 + num3) / 3
print("The average of the three numbers is: ", average)

