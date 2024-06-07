# Define a list of favorite colors
favorite_colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']

# Create a new list using a for loop
colors_list = []
for color in favorite_colors:
    colors_list.append(color)

print("List of favorite colors:", colors_list)


# Initial input number
number = 12345
# Convert the number to a string to allow reversing
num_str = str(number)

# Initialize variables for the reversed number and the index
reversed_num_str = ""
index = len(num_str) - 1

# Use a while loop to reverse the number
while index >= 0:
    reversed_num_str += num_str[index]
    index -= 1

# Convert the reversed string back to an integer
reversed_number = int(reversed_num_str)

print("Reversed number:", reversed_number)
