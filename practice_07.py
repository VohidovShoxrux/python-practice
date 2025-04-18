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

# 18.04.2025

# 55

# def count_words(text):
#     return len(text.split())

# print(count_words(input("Textni kiriting: ")))

# 56

# def find_shortest_word(text):
#     words = text.split()
#     shortest_word = words[0]

#     for word in words:
#         if len(word) < len(shortest_word):
#             shortest_word = word

#     return f"{shortest_word} {len(shortest_word)}" 

# text = input("Textni kiriting: ")

# print(find_shortest_word(text))

# 57 dastur

# def Title(text):
#     return text.title()

# 58

# def remove_extra_space(text):
#     text = " ".join(text.split())
#     return text

# print(remove_extra_space("gar   sog'insam       seni        na      qilay"))

# 59

# def extract_name(text):
#     paths = text.split("/")
#     filepath = paths[-1]

#     file = filepath.split(".")[0]
#     return file

# text = input("Faylni liriting: ")
# print(extract_name(text))
  
# 60 
# def extract_extention(text):
#     return text.split(".")[-1]

# text = input("Faylni kiriting: ")

# print(extract_extention(text))

# 61 

# def extract_first_file_path(text):
#     paths = text.split("/")
#     if len(paths)>2:
#         res = paths[1]
#     else:
#         res = "/"

#     return res

# text = input("Fileni kiriting: ")

# print(extract_first_file_path(text))

# 62

# def extract_first_file_path(text):
#     paths = text.split("/")
#     if len(paths)>3:
#         res = paths[-2]
#     else:
#         res = "/"

#     return res

# text = input("Fileni kiriting: ")

# print(extract_first_file_path(text))

# 63 

# def check_alpha(text):
#     letters = [char for char in text if char.islower()]

#     for i in range(1, len(letters)):
#         if letters[i] < letters[i-1]:
#             return letters[i]
        
#     return 0

# text = input("Text kiriting: ")

# print(check_alpha(text))

# 64 

# def check_paran(text):
#     balance = 0

#     for index, char in enumerate(text):
#         if char == "(":
#             balance += 1
#         elif char == ")":
#             balance -= 1
#         if balance < 0:
#             return f"Xatolik: {index}-indeksta yopilmagan qavs."

#     if balance > 0:
#         return "Xatolik: ochilgan qavs yopilmagan."
#     else:
#         return "Qavslar to‘g‘ri joylashgan."

# text = input("Matnni kiriting: ")
# print(check_paran(text))
