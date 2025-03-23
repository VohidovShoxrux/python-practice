# 23.03.2025
# vohidov

# 42 insertion sort algorithm

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        current_value = arr[i]
        position = i-1

        while position >= 0 and arr[position] > current_value:
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = current_value
    
    return arr

print(insertion_sort([4,6,2,1,7]))