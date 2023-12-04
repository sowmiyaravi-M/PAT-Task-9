#  Lambda function to find every element in the list is an integer or string
list = [1, 'hello', 42, 'world', 7]

result = all(isinstance(elem, (int, str)) for elem in list)

if result:
    print("All elements are either integers or strings.")
else:
    print("Not all elements are either integers or strings.")
