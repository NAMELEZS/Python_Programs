### 03/28/2021
### Norman Lowery II
### Looping through a list

months = ['january ', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

# Using a for loop to print a list
# I can use the name after for such as "month" i can name that whatever i want and then i use my lists name to loop, then i can print the name i chose to give such as "month"
for month in months:
    print(month.title() + "\n")
    print("The next month is: ")

print("Goodbye")