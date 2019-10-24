# lab exam
import string


def make_new_row(old_row):
    """ Requires:
        -- list old_row that begins and ends with a 1 and has zero or more
            integers in between (has to have at least [1,1])       
        Returns:       
        -- list beginning and ending with a 1 and each interior (non 1)          
            integer is the sum of the corresponding old_row elements         
            For example if old_row = [1,4,6,4,1], then new_row = [1,5,10,10,5,1],          
            i.e. 5=1+4, 10=4+6, 10=6+4, 5=4+1 """

    new_row = [1]

    if old_row == [0]:
        return [1]
    elif old_row == [1]:
        return [1, 1]
    else:
        for i in range(1, len(old_row)):
            new_row.append(old_row[i-1] + old_row[i])

        new_row.append(1)
        return new_row


# Bool to make sure a correct integer is entered
height_valid = False
while not height_valid:
    height = input("Enter the desired height of Pascal's Triangle: ")
    height = int(height)

    if height < 0:
        print("Invalid input, enter something greater than 0")
    else:
        height_valid = True

# Setting these variables so they print properly
row = make_new_row([1, 1])
L = [[1], [1, 1], [1, 2, 1]]

# Printing the lists
print("Printing lists line by line: ")
if height == 1:
    print(make_new_row([0]))
elif height == 2:
    print(make_new_row([0]))
    print(make_new_row([1]))
else:
    print(make_new_row([0]))
    print(make_new_row([1]))
    print(row)
    for i in range(2, height - 1):
        row = make_new_row(row)
        print(row)
        L.append(row)

# Print the list on one line
print("Printing list on one line: ")
for j in range(0, height):
    print(L[j], end='')
print("")

# Converting the list to a string
list_str = ' '.join([str(i) for i in L])
bad_chars = string.whitespace + string.punctuation
new_str = list_str

for char in new_str:
    if char in bad_chars:
        new_str = new_str.replace(char,"")

print(new_str.center(100))
