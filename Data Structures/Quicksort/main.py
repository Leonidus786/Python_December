# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1

#     for j in range(low, high):
#         if array[j] <= pivot:
#             i += 1
#             array[i], array[j] = array[j], array[i]

#     array[i+1], array[high] = array[high], array[i+1]
#     return i+1

# def quicksort(array, low=0, high=None):
#     if high is None:
#         high = len(array) - 1

#     if low < high:
#         pivot_index = partition(array, low, high)
#         quicksort(array, low, pivot_index-1)
#         quicksort(array, pivot_index+1, high)

# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# quicksort(my_array)
# print("Sorted array:", my_array)






def partition(array, low, high):
    """
    Partitions the array around a pivot element.
    Args:
        array (list): The input list to be partitioned.
        low (int): The starting index of the subarray.
        high (int): The ending index of the subarray.
    Returns:
        int: Index of the pivot element after partitioning.
    """
    pivot = array[high]  # Select the pivot (usually the last element)
    i = low - 1  # Initialize the index for elements less than or equal to the pivot

    for j in range(low, high):
        if array[j] <= pivot:
            # Swap elements if they are less than or equal to the pivot
            i += 1
            array[i], array[j] = array[j], array[i]

    # Place the pivot in its correct position
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort(array, low=0, high=None):
    """
    Recursively sorts the input array using quicksort.
    Args:
        array (list): The input list to be sorted.
        low (int): The starting index of the subarray (default is 0).
        high (int): The ending index of the subarray (default is len(array) - 1).
    """
    if high is None:
        high = len(array) - 1

    if low < high:
        # Find the pivot index and sort the left and right subarrays
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)
