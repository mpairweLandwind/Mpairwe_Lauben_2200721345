squares = [x**2 for x in range(10)]
print(squares)

# a list of even  squares in the range of 20
even_squares = [x**2 for x in range(20) if (x**2) % 2 == 0]
print(even_squares)

# Create a dictionary where key is the number and value is the cube of the number for numbers between 1 and 10
dict_of_cubes = {x: x**3 for x in range(1, 11)}

# Convert the dictionary items to a list of tuples
list_of_tuples = list(dict_of_cubes.items())
print(list_of_tuples)


