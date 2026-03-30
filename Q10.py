number = float(input("Enter a decimal number :"))

integer_part = int(number)

decimal_part = int((number - integer_part) * 100)

print("Integer part :", integer_part)
print("Decimal part :", decimal_part)
