def find_max(num_list):
    largest = num_list[0]
    for num in num_list:
        if num > largest:
            largest = num
    return largest


