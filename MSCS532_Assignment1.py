def insertion_sort_desc(array_list):
    # traverse fron 1 to length of given array_list
    for i in range(1, len(array_list)):
        current_value = array_list[i]
        j = i - 1
        while j >= 0 and array_list[j] < current_value:
            array_list[j + 1] = array_list[j]
            j -= 1
        array_list[j + 1] = current_value
    return array_list   


# Sample Example
array_list = [8, 2, 3, 4, 5, 6, 8, 10, 12]
insertion_sort_desc(array_list)
print("Sorted array list using Insertion Sort Algorithm in monotonically decreasing order:", array_list)