user_input = input("Enter some text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + '\n')

extra_input = input("Enter more text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(extra_input + '\n')

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    contents = file.read()
    print(contents)
