# 19.03.2025
# vohidov

#34

# def array_pattern(arr):

#     n = len(arr)

#     left = 0
#     right = n - 1
#     result = []

#     while left <= right:
#         result.append(arr[left])
#         left += 1

#         if left <= right:
#             result.append(arr[right])
#             right -= 1
        
#     return result

# print(array_pattern(list(range(10))))

# 35

# def array_pattern(arr):

#     n = len(arr)

#     left = 0
#     right = n - 1
#     result = []

#     while left <= right:
        
#         if left <= right:
#             result.append(arr[left])
#             left += 1

#         if left <= right:
#             result.append(arr[left])
#             left += 1

#         if left <= right:
#             result.append(arr[right])
#             right -= 1
        
#         if left <= right:
#             result.append(arr[right])
#             right -= 1
        
#     return result

# print(array_pattern(list(range(10))))

# 36

# def find_small_local_maxima(arr):

#     n = len(arr)
#     local_maximas = []

#     for i in range(1, n-1):
#         if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
#             local_maximas.append(arr[i])
    
#     if local_maximas:
#         return min(local_maximas)
#     else:
#         return None

# print(find_small_local_maxima([1,3,2,4,6,5,9,1]))
# print(find_small_local_maxima([1,11,2,4,6,5,9,1]))

# 37

# def find_closest(arr, r):
#     min_diff = float("inf")

#     for element in arr:
#         diff = abs(element - r) # faqat musbat son qaytaradi qisqacha matematikadagi modul

#         if diff < min_diff:
#             min_diff = diff
#             closest_element = element
        
#     return closest_element

# print(find_closest([1,3,2,4,6,5,9, 1],5))
# print(find_closest([1,3,2,4,6,11,9,1],5))

# 38

# def find_numbers_frequency(arr):
#     numbers = []
#     frequency = []

#     for element in arr:
#         if element in numbers:
#             index = numbers.index(element)
#             frequency[index] += 1
#         else:
#             numbers.append(element)
#             frequency.append(1)
        
#     for i in range(len(numbers)):
#         print(f"{numbers[i]} soni {frequency[i]} ta")
    
#     print(f"numbers: {numbers}")
#     print(f"frequency: {frequency} ")

# find_numbers_frequency([1,3,2,4,2,1,9,1])

# 39

# import random

# def select_random_numbers(n, m):

#     if n > m:
#         return "n soni m sonidan kichik bo'lsin"

#     selected_numbers = random.sample(range(1, m+1,), n)
#     return selected_numbers

# print(select_random_numbers(3,15))

# 40 bubble sort algorithm

# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
    
#     return arr

# print(bubble_sort([7,2,9,3,1,5,4,8,6,]))

# 41 selection sort algorithm

# def selection_sort(arr):

#     n = len(arr)

#     for i in range(n):

#         min_index = i

#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr

# print(selection_sort([7,2,9,3,1,5,4,8,6,]))



