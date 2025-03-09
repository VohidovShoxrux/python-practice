# 09.03.2024
# vohidov

# 11. sonning butun va qoldiq qosmini bo'lish amallarisiz topish

# n = int(input("N: "))
# m = int(input("M: "))

# butun = 0

# while n>=m:
#     n -= m
#     butun += 1

# qoldiq = n

# print(f"qoldiq: {qoldiq}, butun: {butun}")

# 12. 

# n = int(input("Nechta son kiritmoqchisiz?: "))
# first_number = int(input("1-sonni kiriting: "))

# max = first_number
# min = first_number

# for _ in range(n-1):
#     current_number = int(input("keyingi sonni kiriting: "))

#     if current_number > max:
#         max = current_number
    
#     if current_number < min:
#         min = current_number

# print(f"eng kichik son: {min} va eng katta son: {max}")

# 13.

# n = int(input("Nechta son kiritmoqchisiz?: "))
# first_number = int(input("1-sonni kiriting: "))

# min = first_number
# index = 1

# for i in range(2,n+1):
#     current_number = int(input(f"{i}-sonni kiriting: "))
    
#     if current_number < min:
#         min = current_number
#         index = i

# print(f"eng kichik son: {min}, va u {index}-da joylashgan")

# 14.

# n = int(input("Nechta son kiritmoqchisiz?: "))
# first_number = int(input("1-sonni kiriting: "))

# max = first_number
# min = first_number

# max_pos = 1
# min_pos = 1 

# for i in range(2,n+1):
#     current_number = int(input(f"{i}-sonni kiriting: "))

#     if current_number >= max:
#         max = current_number
#         max_pos = i

#     if current_number < min:
#         min = current_number
#         min_pos = i

# print(f"birinchi uchragan eng kichik son: {min} va u {min_pos}-da joylashgan")
# print(f"oxirgi uchragan eng katta son: {max} va u {max_pos}-da joylashgan")

# 15.

# n = int(input("Nechta son kiritmoqchisiz?: "))
# first_number = int(input("1-sonni kiriting: "))

# max = first_number
# min = first_number

# max_pos = 1
# min_pos = 1 

# for i in range(2,n+1):
#     current_number = int(input(f"{i}-sonni kiriting: "))

#     if current_number > max:
#         max = current_number
#         max_pos = i

#     if current_number < min:
#         min = current_number
#         min_pos = i

# if max_pos > min_pos:
#     print(min, min_pos)
# else:
#     print(max, max_pos)

# 16.

# n = int(input("Nechta son kiritmoqchisiz?: "))
# first_number = int(input("1-sonni kiriting: "))

# max = first_number
# min = first_number

# max_pos = 1
# min_pos = 1 

# for i in range(2,n+1):
#     current_number = int(input(f"{i}-sonni kiriting: "))

#     if current_number >= max:
#         max = current_number
#         max_pos = i

#     if current_number <= min:
#         min = current_number
#         min_pos = i

# if max_pos < min_pos:
#     print(min, min_pos)
# else:
#     print(max, max_pos)