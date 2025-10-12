# From a list
list_example = [1, 2, 2, 3, 4]
set_from_list = set(list_example)

# From a tuple
tuple_example = (2, 3, 3, 4, 5)
set_from_tuple = set(tuple_example)

# From a dictionary
dict_example = {"a": 1, "b": 2, "c": 3}
set_from_dict = set(dict_example)  # This will contain only the keys

print("Set from list:", set_from_list)
print("Set from tuple:", set_from_tuple)
print("Set from dictionary:", set_from_dict)
