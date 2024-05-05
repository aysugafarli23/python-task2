# Əlavə olaraq indiyə qədər nə  keçmişiksə onlardan istifadə edəbilərsiz. Uğurlar.

# tasks for define function 

# 1.) verilmiş listdəki ədədlərin hansılarının hər hansı
# bir ədədin kvadratı olduğunu define funksiyasında yazıb 
# və listin içərisində ekrana çıxarın. 

# import math

# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]
# newlist = []

# def checkFunc():  
#     for number in mylist:
#         # root = math.sqrt(number)
#         if number>0 and math.sqrt(number) ** 2 == abs(number):
#           newlist.append(math.sqrt(number))
#     print(newlist)    
# checkFunc()


#  2)Funksiya yazin list qebul etsin 
# ve tekrarlanmayan elementleri bizə qaytarsın:
#  input:[-1,1,2,2,6,7,7,'say']

    
    
# def unique_list():    
#     raw_data = input().strip("[]").replace("'", "")
#     data = [item for item in raw_data.split(",")]
#     new_data = set(data)
#     print( new_data)

# unique_list()




# 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini
# icra edən funksiya yazın


# from functools import reduce

# def unique_list():    
#     raw_data = input().strip("[]").replace("'", "")
#     data = [int(item) for item in raw_data.split(" ")]
#     new_data = set(data)
#     print( new_data)
    
#     result = reduce((lambda x, y: x * y), new_data) 
#     print(result) 
    

# unique_list()




# 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın

# a = 10
# items = [ i for i in range(1, a + 1) if a % i == 0]
# print(items)
        


# 5)Əlininzdə ayların olduğu bir list var 
# siz ay qarşısında uzunluğu olduğu bir dictionary yaradın 
# və bunu comprehension ilə edin və alınan listi print etdirin.

# mənim listim
# mylist=['may','iyun','iyul']
# bu şəkildə olacaq
# {'may': 3, 'iyun': 4, 'iyul': 4}


#Comprehensive way
months = ['may','iyun','iyul']
month_lengths = {month: len(month) for month in months}
print(month_lengths)



#Normal way
# months = ['may', 'iyun', 'iyul']
# month_lengths = {}

# for month in months:
#     month_lengths[month] = len(month)
# print(month_lengths)




# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu 
# və kiçik hərflərlə yazıldığı list düzəldin 
# və bunu conprehension ilə edin (əlavə olaraq funksiya da 
# istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']


# people = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# names = [name.lower().split()[::-1][1] for name in people]
# print(names)



# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# results=[ 2.5, 3.5, 4.5]

# def calculate_averages():
#     nums1 = [1, 2, 3]
#     nums2 = [4, 5, 6]
#     results = []

#     for idx1, val1 in enumerate(nums1):
#         for idx2, val2 in enumerate(nums2):
#             if idx1 == idx2:
#                 avg = (val1 + val2) / 2
#                 results.append(avg)
#     print("Results: ", results)
    
    
# calculate_averages()