# 12.03.2025
# vohidov

# 17.

# n = int(input("Nehcta son kiritmoqchisiz?: "))
# first_number = int(input("1-sonni kiriting: "))

# min_value = float("inf")

# if first_number > 0:
#     min_value = first_number

# for i in range(2, n+1):
#     current_number = int(input(f"{i}-sonni kiriting: "))

#     if 0 < current_number < min_value:
#         min_value = current_number

# if min_value == float("inf"):
#     print(0)
# else:
#     print(min_value)

# 18.

# n = int(input("Nehcta son kiritmoqchisiz?: "))
# first_number = int(input("1-sonni kiriting: "))

# max_value = None
# max_pos = -1

# if first_number %2 != 0:
#     max_value = first_number
#     max_pos = 1

# for i in range(2, n+1):
#     current_number = int(input(f"{i}-sonni kiriting: "))

#     if current_number % 2 != 0:
#         if max_value is None or current_number > max_value:
#             max_value = current_number
#             max_pos = i

# if max_value is None:
#     print(0)
# else:
#     print(max_value, max_pos)

# 19. 

# n = int(input("Nehcta son kiritmoqchisiz?: "))
# first_number = int(input("1-sonni kiriting: "))

# max_value = first_number
# max_value = 1

# for i in range(2, n+1):
#     current_number = int(input(f"{i}-sonni kiriting: "))

#     if current_number >= max_value:
#         max_value = current_number
#         max_pos = i

# next_elements_count = n - max_pos

# print(max_value, next_elements_count)

# 20. 

# n = int(input("Nehcta son kiritmoqchisiz?: "))
# first_number = int(input("1-sonni kiriting: "))
# second_number = int(input("2-sonni kiriting: "))

# if first_number < second_number:
#     min1, min2 = first_number, second_number
# else:
#     min1, min2 = second_number, first_number

# for i in range(3, n + 1):
#     current_number = int(input(f"{i}-sonni kiriting: "))

#     if current_number < min1:
#         min2 = min1
#         min1 = current_number
#     elif current_number < min2:
#         min2 = current_number

# print(min1, min2)

# 21. 

# n = int(input("Nehcta son kiritmoqchisiz?: "))
# first_number = int(input("1-sonni kiriting: "))
# second_number = int(input("2-sonni kiriting: "))

# max_sum = first_number + second_number
# prev_number = second_number

# for i in range(3, n + 1):
#     current_number = int(input(f"{i}-sonni kiriting: "))

#     current_sum = prev_number + current_number

#     if current_sum > max_sum:
#         max_sum = current_sum

#     prev_number = current_number

# print(max_sum)

# 22. 

# def is_prime(n):
#     if n < 2:
#         return False
    
#     for i in range(2, n):
#         if n % i == 0:
#             return False
    
#     return True

# k = int(input(f"Nechta son kiritmoqchisiz? (k>0): "))

# prime_count = 0

# for i in range(1, k + 1):
#     n = int(input(f"{i}-sonni kiriting: "))

#     if is_prime(n):
#         prime_count += 1

# print(prime_count) 

# 23

# def digit_count(k):

#     count = 0

#     while k>0:
#         k = k // 10
#         count += 1
    
#     return count

# number = int(input("sonni kiriting: "))
# print(digit_count(number))