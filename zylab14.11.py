"Peter Nguyen"
"6/27/2021"
"CIS2348"
"1860823"
"14.11 CIS 2348 LAB: Descending selection sort with output during execution"

def selection_sort_descend_trace(lst):
    for i in range(len(lst) - 1):
        largest_value_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[largest_value_index]:
                largest_value_index = j
        lst[i], lst[largest_value_index] = lst[largest_value_index], lst[i]
        for x in lst:
            print(x, end=' ')
        print()
    return lst

if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)