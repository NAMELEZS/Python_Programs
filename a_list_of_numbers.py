### 03/28/2021
### Norman Lowery II
### Creating a list of numbers

numbers = list(range(1,6))
print(numbers)

odd_numbers = list(range(1,101, 2))
print(odd_numbers)


squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)