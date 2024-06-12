student_info = {
    "name": "mpairwe lauben",
    "age": "76",
    "technology": "AI",
    "course": "CMP",
    "year": "year5"
}

print(student_info['name'])  # Output: mpairwe lauben

# Updating values in the dictionary
student_info['name'] = 'alien yu yen'
student_info['technology'] = 'embedded systems'
student_info['course'] = 'BscTEL'

print(student_info)

# Removing a key-value pair using del
del student_info['year']

print(student_info)

# Removing a key-value pair using pop
removed_value = student_info.pop('age')

print(student_info)
print(f'Removed value: {removed_value}')


# Updating values using the update method
student_info.update({
    'course': 'BSSE',
    'whatsapp_number': '+1234567890'
})

print(student_info)