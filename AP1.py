data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))

# Excepted output
[10, 501, 22, 37, 100, 999, 87, 351]


'''In this case, all elements in the original list are greater than 4,
 so the filter function doesn't remove any elements,
   and the output is the same as the original list.'''






