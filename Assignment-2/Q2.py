# Write a function that takes 2 integers a and b and print all even number btw them

def print_even_between(a, b):
    start = min(a, b)
    end = max(a, b)
    
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

print_even_between(2,10)