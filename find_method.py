### 03/28/2021
### Norman Lowery II
### 

# Python starts counting at "0-1-2-3-4" instead of "1-2-3-4". .find only shows the number of what you are trying to find
my_book = "My favorite book is 'Elon Musk'.".find('Elon')
print(my_book)

# Must use the exact word or symbol with find to work
subject = "$$$ Get Rich Now $$$".find('$$$')
print(subject)