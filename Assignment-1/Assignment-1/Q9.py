Principle = int(input("Enter the Principle value: "))
Rate = int(input("Enter the Rate value: "))
Time = int(input("Enter the time value: "))

p = float(Principle)
r = float(Rate)
t = float(Time)

Interest = (p * r * t)/100

print("The calculated Simple Interest is :", Interest)