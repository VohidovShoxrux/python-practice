# 07.03.2025
# vohidov

# 1. uch ta sondan kichigini topuvchi dastur

# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# if a < b and a < c:
#     print(a)
# elif b < a and b < c:
#     print(b)
# else:
#     print(c)

# 2. kabisa yilini topuvchi dastur

# year = int(input("yilni kiriting: "))

# if (year%4 == 0 and year%100 != 0) or year % 400 == 0:
#     print(366)
# else:
#     print(365)

# 3. 

# x =int(input("1-sonni kiriting(x):"))
# y =int(input("2-sonni kiriting(y):"))

# min = (x+y)/2
# max = 2*x*y

# if x > y:
#     x, y = max, min
# elif x < y:
#     x, y = min, max

# print(f"{x} {y}")

# 4. input(today) = tomorrow

# day = int(input("Kunni kiriting: "))
# month = int( input("Oyni kiriting: "))

# day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# if month < 1 or month > 12:
#     print("Bunday oy qo'q")
# elif day < 1 or day > day_in_month[month-1]:
#     print("Bunday sana yo'q")
# else:
#     if day == day_in_month[month-1]:
#         month +=1
#         day +=1
#     else:
#         day +=1

#     if month > 12:
#         month = 1 
    
# print(f"{day:02}/{month:02}")

# 5. n gacha bo'lagan mukammal sonlar

# N = int(input("N kiriting: "))

# perfect_numbers = []

# def find_sum_of_devisor(num):
#     total = 0

#     for i in range(1,num):
#         if num % i == 0:
#             total += i
    
#     return total

# for number in range(2, N+1):
#     if number == find_sum_of_devisor(number):
#         perfect_numbers.append(number)
    
# print(*perfect_numbers)

# 6. n natural son berilgan. shu songacha bo'lgan tub sonalrni chiqaruvchi dastur 

# N = int(input("N sonini kiriting: "))

# prime_numbers = []

# for number in range(2, N + 1):

#     is_prime = True

#     for  devisor in range(2, number):
#         # print(devisor,number)
#         if number % devisor == 0:
#             is_prime = False
        
#     if is_prime:
#         prime_numbers.append(number)
    
# print(*prime_numbers)

# 7. N sonigacha bo'lgan dost sonlar 

# N = int(input("N sonni kiriting: "))

# def sum_of_devisor(number):
#     total = 0

#     for i in range(1, number):
#         if number % i == 0:
#             total += i
    
#     return total

# amicable_pairs = []

# for a in range(1, N+1):
#     b = sum_of_devisor(a)

#     if a < b <= N and a == sum_of_devisor(b):
#         amicable_pairs.append((a,b))

# for pair in amicable_pairs:
#     print(pair[0],pair[1])

# 8. 

# starter = int(input("Boshlang'ich summani kiriting: "))
# p = int(input("Foizni kiriting: "))

# current = starter
# month = 0

# while current <= 2*starter:
#     current += current*p/100
#     month += 1

# print(f"{month} oyda {current} so'm")

# 9. sondagi raqamlar yig'indsini

# number = int(input("sonni kiriting: "))

# digit_count = 0
# digit_sum = 0

# while number > 0:
#     digit_sum += number % 10
#     number = number // 10

#     digit_count += 1

# print(digit_count, digit_sum)

# 10. Evklid algoritmi bo'yicha EKUB

# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))

# while B !=0:
#     print(A,B)
#     A, B = B, A % B

# print(f"EKUB {A}")