# TO-DO: complete the helper function below to merge 2 sorted arrays

# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    j = 0
    k = 0

    # Your code here
    for i in range(elements):

        if j > len(arrA)-1:
            merged_arr[i:] = arrB[k:]
            break
        elif k > len(arrB)-1:
            merged_arr[i:] = arrA[j:]
            break
        elif arrA[j] <= arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        else:
            merged_arr[i] = arrB[k]
            k += 1
    return merged_arr


# arr1 = [3, 7, 8, 10]
# arr2 = [1, 2, 3, 4]
# arr3 = [0, 11, 12, 14]

# print(merge(arr1, arr2))
# print(merge(arr1, arr3))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    sorted_L = merge_sort(left)
    sorted_R = merge_sort(right)
    merged = merge(sorted_L, sorted_R)
    print("merged", merged)
    return merged


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1

    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):

        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r):

        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
