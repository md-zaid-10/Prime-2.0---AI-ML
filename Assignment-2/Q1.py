# WAP that takes salary as input. Using conditional statement, calculate the final tax rate based on these rules:
'''
 - if salary < 30000 = 5%
 - if salary is 30000-70000 = 15%
 - if salary > 70000 = 25%
'''

salary = int(input("Enter your salary: "))

if (salary <= 30000):
    print("Your final Tax rate is 5%")
elif( 30000 < salary < 70000):
    print("Ypur final Tax rate is 15%")
elif (salary >= 70000):
    print("Ypur final tax rate is 25%")
