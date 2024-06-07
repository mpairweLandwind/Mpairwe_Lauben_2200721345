print('hello world, welcome to the future')

full_name = input("Enter full name: ")
course = input("Input Course Programme: ")
honed_skills = input("List skills developed during course journey (comma-separated): ")

# Split the input into a list of skills
skills_list = honed_skills.split(',')

# Join the list of skills into a string with  comma 
skills_str = ', '.join(skills_list[:-1]) + ' and ' + skills_list[-1] if len(skills_list) > 1 else honed_skills

# Print the formatted string
print(f'Am {full_name}, pursuing {course} at Makerere University. During my course journey, I have honed the following skills: {skills_str}.')
