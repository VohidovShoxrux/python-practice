# 23.03.2025
# vohidov

# 42 insertion sort algorithm

# def insertion_sort(arr):
#     n = len(arr)

#     for i in range(1, n):
#         current_value = arr[i]
#         position = i-1

#         while position >= 0 and arr[position] > current_value:
#             arr[position + 1] = arr[position]
#             position -= 1
#         arr[position + 1] = current_value
    
#     return arr

# print(insertion_sort([4,6,2,1,7]))

# 43

# def find_ser(arr):

#     B = []
#     C = []

#     n = len(arr)
#     current_value = arr[0]
#     count = 1
#     for i in range(1, n+1):
#         if i < n and arr[i] == current_value:
#             count +=1
#         else:
#             B.append(count)
#             C.append(current_value)

#             if i < n:
#                 current_value = arr[i]
#                 count = 1

#     return B, C

# resultB1 , resultC1 = find_ser([1,1,1,2,2,3,4,5,5,5])
# print(f"B:{resultB1}\nC:{resultC1}")

# 44

# def spiral_matrix(m, n):
#     elements = list(range(1, m*n+1))

#     matrix = [elements[i * n : (i + 1) *n] for i in range(m)]

#     for i in range(m):
#         if i%2 == 1:
#             matrix[i] = matrix[i][::-1]
#     print(matrix)

# spiral_matrix(4,3)

# 45

# def transform_matrix(m):
#     elements = list(range(1, m * m + 1))
#     matrix = [elements[i * m : (i + 1) * m] for i in range(m)]

#     print("Original matrix")

#     for row in matrix:
#         print(row)
    
#     new_list = []
#     used_elements = set()

#     for i in range(m):
#         row = []

#         for elem in matrix[i]:
#             if elem not in used_elements:
#                 row.append(elem)
#                 used_elements.add(elem)
        
#         for j in range(i+1,m):
#             column_elem = matrix[j][m-1-i]
#             if column_elem not in used_elements:
#                 row.append(column_elem)
#                 used_elements.add(column_elem)
        
#         new_list.append(row)

#     return new_list

# transformed3 = transform_matrix(3)

# for row in transformed3:
#     print(*row)


# transformed4 = transform_matrix(4)

# for row in transformed4:
#     print(*row)

# 46 

# def find_sumof_matrix(m, n):
    
#     elements = list(range(1, m * n+1))
#     matrix = [elements[i * n:(i + 1) * m] for i in range(m)]

#     for row in matrix:
#         sumofrow = sum(row)
        
#         print(f"{row}=>{sumofrow}")

# find_sumof_matrix(3, 3)

# 47

# def find_mult(m, n): # m=row , n=column
#     elements = list(range(1, m * n + 1))
#     matrix = [elements[i * n: (i+1)*m] for i in range(m)]

#     for row in matrix:
#         print(row)

#     column_products = [1] * n

#     for col in range(n):
#         for row in range(m):
#             column_products[col] *= matrix[row][col]

#     print(column_products) 
# find_mult(3,3)

# 48

# def compare_row(matrix):
#     for row_index, row in enumerate(matrix):

#         count_positive = sum(1 for num in row if num > 0)
#         count_negative = sum(1 for num in row if num < 0)

#         if count_positive == count_negative:
#             return row_index + 1
    
#     return "Bunday qator yo'q"

# matrix1 = [[-1, -2, 3], [-4, 0, 6], [7, 8,9]]
# matrix2 = [[1,2,3],[4,0,6],[7,8,9]]

# print(compare_row(matrix1))
# print(compare_row(matrix2))

# 49 

# def find_max_row(matrix):
#     for row in matrix:
#         print(f"{row}=>{max(row)}")

# matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
# matrix2 = [[9,2,5], [9,2,9], [4,5,2]]
# find_max_row(matrix1)
# find_max_row(matrix2)

# 50 

# def find_max_column(matrix):

#     m = len(matrix)
#     n = len(matrix[0])

#     for col in range(n):
#         column = []

#         for row in range(m):
#             column.append(matrix[row][col])

#         print(max(column))
    
# matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
# matrix2 = [[1,2,9],[4,8,6],[7,5,3]]

# find_max_column(matrix1)
# find_max_column(matrix2)

# 51

# def find_min_index(matrix):
#     min_value = float("inf")
#     min_index = (0, 0)

#     m = len(matrix)
#     n = len(matrix[0])

#     for row in range(m):
#         for col in range(n):
#             if matrix[row][col] < min_value:
#                 min_value = matrix[row][col]
#                 min_index = (row, col)
    
#     return min_index

# matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
# matrix2 = [[9,2,9],[4,1,6],[7,5,3]]

# print(*find_min_index(matrix1))
# print(*find_min_index(matrix2))

52

def remove_min_column(matrix):
    min_vlaue = float("inf")
    min_col = 0

    m = len(matrix)
    n = len(matrix[0])

    for row in range(m):
        for col in range(n):
            if matrix[row][col] <  min_vlaue:
                min_vlaue = matrix[row][col]

    new_matrix = []

    for row in matrix:
        new_row = [row[j] for j in range(len(row)) if j !=min_col]
        new_matrix.append(new_row)

    return new_matrix

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[9,2,8],[4,1,6],[7,5,3]]

result1 = remove_min_column(matrix1)
result2 = remove_min_column(matrix2)

print("Mtrix 1")
for row in result1:
    print(row)

print("Mtrix 2")
for row in result2:
    print(row)