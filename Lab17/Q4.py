# Given a dictionary with a values list, extract the key whose value has the most unique
# values.
# Input: test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
# Output:"Best"
# Explanation:3 (max) unique elements, 9,6,5 of "Best"

max_key = " "
max_unique_count = 0

# Loop through dictionary
for key, val_list in test_dict.items():
    unique_count = len(set(val_list))  # unique elements count
    if unique_count > max_unique_count:
        max_unique_count = unique_count
        max_key = key

print("Key with most unique values:", max_key)