import math

num = float(input("Enter a number: "))


if num < 0:
    print("Square root and natural log are not defined for negative numbers.")
else:
    sqrt_result = math.sqrt(num)
    log_result = math.log(num)
    sin_result = math.sin(num)  

print(f"Square root of {num} is {sqrt_result}")
print(f"Natural logarithm (ln) of {num} is {log_result}")
print(f"Sine of {num} radians is {sin_result}")
