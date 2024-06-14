def get_person_details():
    name = "Am Mpaiwe Lauben"
    year = "Year2"
    occupation = "Software Programmer"
    age = "76 yrs"
    return name, year, occupation,age


details = get_person_details()
formatted_details = "{} {}  {}, {} old".format(*details)
print(formatted_details)


# lambda Expressions

add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# using lambda in sorting function
points = [(2, 3), (1, 2), (4, 1)]
points.sort(key=lambda point: point[1])
print(points)

# define a function to get user info that accepts arbitrary  keyword arguments and prints ecah key value pair
def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

get_user_info(name="mpairwe lauben", age=47, email="mpairwelauben375@gmail.com", country="Uganda")
