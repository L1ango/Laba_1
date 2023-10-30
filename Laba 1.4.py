#Напишите программу для слияния нескольких словарей в один.
dict1 = {'Reques': 1, 'cut': 2}
dict2 = {'in': 3, 'pa': 4}
dict3 = {'ce': 5}

merged_dict = {**dict1, **dict2, **dict3}

print(merged_dict)
