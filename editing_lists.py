### 03/28/2021
### Norman Lowery II
### Editing lists

birthday_months = ['spril', 'may', 'november']

print(birthday_months)

# Can use this to edit your spelling mistake
birthday_months[0] = 'april'

print(birthday_months)

# Can use the .append() method to add whatever you want to the list
birthday_months.append('june')

print(birthday_months)

birthday_months = []

print(birthday_months)

birthday_months.append('august')

print(birthday_months)

# You can use .insert method to put whatever you want into the specific spot you want
birthday_months.insert(0, 'may')

print(birthday_months)

# Can use the del method to delete any spot you want
del birthday_months[1]

print(birthday_months)