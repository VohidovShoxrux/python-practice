#16.04.2025

# 53
# def remove_min_row(matrix):
#     min_value = float("inf")
#     min_row = 0

#     for row in range(len(matrix)):
#         for col in range(len(matrix[0])):
#             if matrix[row][col] < min_value:
#                 min_value = matrix[row][col]
#                 min_row = row
    
#     new_matrix = [matrix[row] for row in range(len(matrix)) if row != min_row]

#     return new_matrix
# matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
# matrix2 = [[9,2,9],[4,1,6],[7,5,3]]

# result1 = remove_min_row(matrix1)
# result2 = remove_min_row(matrix1)

# print("Matrix1")
# for row in result1:
#     print(*row)

# print("Matrix2")
# for row in result2:
#     print(*row)

# 54

# def extract_str(text):

#     if text.count(" ") == 1:
#         return ""

#     first_space_index = text.find(" ")
#     last_space_index = text.rfind(" ")

#     if first_space_index != -1 and last_space_index != -1 and first_space_index != last_space_index:
#         res = text[first_space_index+1: last_space_index]
#     else:
#         res = ""

#     return res

# text = input("Textni kiriting: ")

# print(extract_str(text))
