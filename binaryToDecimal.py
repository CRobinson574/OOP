# program to convert a binary number to a decimal
binary_str = input("Enter a binary number\n")

binary_str = binary_str[::-1]

decimal = 0
index = 0

for i in binary_str:
    decimal += int(i) * pow(2, index)
    index = index + 1

print("Decimal is: ",decimal)

