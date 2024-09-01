def insertion_sort_desc(array_list):
    for i in range(1, len(array_list)):
        current_value = array_list[i]
        j = i - 1
        while j >= 0 and array_list[j] < current_value:
            array_list[j + 1] = array_list[j]
            j -= 1
        array_list[j + 1] = current_value


# Sample Example
array_list = [1, 2, 3, 4, 5, 6, 8, 10, 12]
insertion_sort_desc(array_list)
print(array_list)
