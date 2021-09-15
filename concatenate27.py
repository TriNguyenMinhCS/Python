def lst_val_data(list):
    result = ''
    for elements in list:
        result += str(elements)
    return result

print(lst_val_data([1, 3, 5, 7]))
