### 03/27/2021
### Norman Lowery II
### Looping through a dictionary

birthday_months = {
    'tony' : 'november' ,
    'pat' : 'june' ,
    'mary' : 'may'
}

print(birthday_months)

# looping through key-value pairs
book_1 = {
    'name' : 'elon musk' ,
    'author' : 'ashlee vance' ,
    'price' : 14.99,
    'publisher' : ' virgin books',
}

for key, value in book_1.items():
    print("\nkey: " + key)
    print("value: " + value)