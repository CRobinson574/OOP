# program to convert a decimal number to binary

num_str = input("Enter a integer to be converted to binary\n")
num = int(num_str)

place = 1
binary = 0

while num > 0:
    remainder = int(num) % 2
    binary = (binary + (remainder * place))
    place = place * 10
    num = int(num) / 2

print("The Binary number is: ", binary)
