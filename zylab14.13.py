"Peter Nguyen"
"6/27/2021"
"CIS2348"
"1860823"
"14.13 CIS 2348 LAB: Sorting user IDs"

# Global variable
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, i, k):
    low = (i - 1)
    mid = (i + k) // 2
    pivot = IDs[mid]
    IDs[mid], IDs[k] = IDs[k], IDs[mid]
    for j in range(i, k):
        if IDs[j] <= pivot:
            low = low + 1
            IDs[low], IDs[j] = IDs[j], IDs[low]
    IDs[low + 1], IDs[k] = IDs[k], IDs[low + 1]
    return (low + 1)


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quisksort() is called
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    if i < k:
        pivot_index = partition(IDs, i, k)
        quicksort(IDs, i, pivot_index - 1)
        quicksort(IDs, pivot_index + 1, k)


if __name__ == "__main__":
    IDs = []
    ID = input()
    while ID != "-1":
        IDs.append(ID)
        ID = input()
    quicksort(IDs, 0, len(IDs) - 1)
    print(num_calls)
    for ID in IDs:
        print(ID)

