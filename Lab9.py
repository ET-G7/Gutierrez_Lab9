# Get the number of rows from the user
num_rows = int(input("Enter the number of rows: "))

# Printing the right-angled triangle
for i in range(1, num_rows + 1):
    for current_number in range(1, i + 1):
        print(current_number, end=' ')
    print()