n1 = float(input("Enter the number :"))
n2 = float(input("Enter the number :"))

add = n1 + n2
sub = n1 - n2
mul = n1 * n2

if n2 != 0:
    div = n1 / n2
else:
    div = "Undefined"

print("\n Results :")
print(f"Addition : {n1} + {n2} = {add}")
print(f"Subtraction : {n1} - {n2} = {sub}")
print(f"Multiplication : {n1} * {n2} = {mul}")
print(f"Division : {n1} / {n2} = {div}")