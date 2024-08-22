# Put the first 10 square numbers in a list using 'range()'

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

###################################################################
# Better way of writing above statement
squares = []
for value in range (1, 11):
    squares.append(value**2)

print(squares)