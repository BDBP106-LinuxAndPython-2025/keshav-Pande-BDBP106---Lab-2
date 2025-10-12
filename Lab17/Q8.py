def interchange_even_odd(lst):
    new_list = lst[:]  # make a copy of the list
    for i in range(0, len(lst) - 1, 2):  # step of 2 to swap pairs
        new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
    return new_list

# Test case
lst = [23, 32, 33, 44, 'BDBH101', 'hello', 'python', 15, 1e-10, True, 'hit']

print("Original list:", lst)
print("List after interchanging even and odd elements:", interchange_even_odd(lst))

