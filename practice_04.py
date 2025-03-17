# 17.03.2025
# vohidov

# 24
# def digit_n(k,n):

#     str_k = str(k)

#     if len(str_k) < n:
#         return -1
#     else:
#         return str_k[n-1]

# number = int(input("Sonni kiriting: "))
# order = int(input("Tartib raqamni kiriting: "))

# print(digit_n(number, order))

# 25    
# def is_polydrome(n):

#     str_n = str(n)

#     return str_n == str_n[::-1]

# def count_poly(numbers):
#     count = 0

#     for number in numbers:
#         if is_polydrome(number):
#             count += 1
    
#     return count

# print(count_poly([12321,123,456]))
# print(count_poly([121,23332,1591]))
# print(count_poly([101,121,131]))

# 26

# def EKUB(a,b):
#     while b != 0:
#         a, b = b, a % b
    
#     return a

# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# print(EKUB(a, b))

# 27
# def EKUB(a,b):
#     while b != 0:
#         a, b = b, a % b
    
#     return a

# def EKUK(a, b):
#     ekuk = a*b / EKUB(a, b)
#     return ekuk

# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# print(EKUK(a, b))

# 28

# def EKUB(a,b):
#     while b != 0:
#         a, b = b, a % b
    
#     return a

# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# def EKUB3(a,b,c):
#     ekub_ab = EKUB(a,b)
#     ekub3 = EKUB(ekub_ab, c)
#     return ekub3

# print(EKUB3(a,b,c))

# 29

# def EKUB(a,b):
#     while b != 0:
#         a, b = b, a % b
    
#     return a

# def EKUB_list(numbers):
#     current_ekub = numbers[0]

#     for number in numbers[1:]:
#         current_ekub = EKUB(current_ekub, number)

#     return current_ekub

# n = int(input("Nechta son kiritmoqchisiz?: "))

# numbers = []

# for i in range(1, n+1):
#     current_number = int(input(f"{i}-sonni kiriting: "))
#     numbers.append(current_number)

# print(EKUB_list(numbers))

# 30

# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# def count_leap_year(years):
#     count = 0

#     for year in years:
#         if is_leap_year(year):
#             count += 1
    
#     return count

# year1 = int(input("1.yilni kiriting: "))
# year2 = int(input("2.yilni kiriting: "))
# year3 = int(input("3.yilni kiriting: "))

# print(count_leap_year([year1, year2, year3]))

# 31 

# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# def month_days(month, year):
#     if month == 2:
#         if is_leap_year(year):
#             return 29
#         else:
#             return 28
#     elif month in [1,3,5,7,8,10,12]:
#         return 31
#     elif month in [4,6,9,11]:
#         return 30
#     else:
#         return -1

# def find_days(year, *months):
#     day_list = [month_days(month, year) for month in months]
#     return day_list

# print(find_days(2020, 2, 11, 12))
# print(find_days(2019, 2, 6, 7))

# 32

# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# def month_days(month, year):

#     if month == 2:
#         if is_leap_year(year):
#             return 29
#         else:
#             return 28
#     elif month in [1,3,5,7,8,10,12]:
#         return 31
#     elif month in [4,6,9,11]:
#         return 30
#     else:
#         return -1 

# def prev_date(day, month, year):

#     if month<1 or month>12:
#         return "Bunday oy mavjud emas"
#     if day< 1 or day > month_days(month,year):
#         return "Bunday snana mavjud emas"
    
#     if day == 1 and month == 1:
#         day = month_days(12, year-1)
#         month = 12
#         year -= 1 
    
#     elif day == 1 and month != 1:
#         month -= 1
#         day = month_days(month, year)
    
#     else:
#         day -= 1

#     return f"{day}/{month}/{year}"

# print(prev_date(29, 2,2019))

# 33

# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# def month_days(moth, year):
#     if moth == 2:
#         if is_leap_year(year):
#             return 29
#         else:
#             return 28
#     elif month in [1,3,5,7,8,10,12]:
#         return 31
#     elif month in [4,6,9,11]:
#         return 30
#     else:
#         return -1

# def next_date(day, month, year):

#     if month<1 or month>12:
#         return "Bunday oy mavjud emas"
    
#     if day < 1 or day > month_days(month, year):
#         return "Bunday sana mavjud emas"

#     if day == month_days(month, year) and month == 12:
#         day = 1
#         month = 1
#         year += 1
#     elif day == month_days(month, year) and month != 12:
#         day = 1
#         month += 1
#     else:
#         day += 1

#     return f"{day}/{month}/{year}"

# print(next_date(28,2,2020)) 

    
