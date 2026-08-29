def duplicates(numbers):
    duplicate = False
    new_list = []

    for num in numbers:
        if num in new_list:
            duplicate = True
        else:
            new_list.append(num)

    return duplicate, new_list


numbers = [1, 2, 3, 2, 4, 5, 1, 6]

result, new_list = duplicates(numbers)

print(result)
print(new_list)