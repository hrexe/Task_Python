#                                     # -----TASK 1 -------------
# cavab = sorted([int(input("Reqem daxil edin:")) for _ in range(5)])
# print(cavab)


                                    # -----TASK 2 -------------
# soz = ' '.join([''.join(sorted(word)) for word in input("cumleni daxil edin:").split()])
# print(soz)


                                    # -----TASK 3 -------------
# eded, cehd = 13, 0
# while (b := int(input("Texmininizi yazin:"))) != eded: cehd += 1
# print(f"Tebrikler {cehd+1} sayida cehde tapdiniz")


                                    # -----TASK 4 -------------

# for i in range(2, 100):  
#     for j in range(2, i):  
#         if i % j == 0:
#             break
#         elif i%j!=0 and i==j+1: 
#             print(f"Sade eded: {i}")
        

                                                    

                                    # -----06/05/2024 -------------


# 1.) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 
# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# print([x for x in mylist if x**0.5 == int(x**0.5)])


#  2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:

# def tekrarlanmayan_elementler(list):
#     tekrarsiz = []
#     for element in list:
#         if list.count(element) == 1:
#             tekrarsiz.append(element)
#     return tekrarsiz

# inputList = [-1, 1, 2, 2, 6, 7, 7, 'say']
# print(tekrarlanmayan_elementler(inputList))


# 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın

# def reqemlerin_hasili(s):
#     hasil = 1
#     for reqem in str(s):
#         if reqem.isdigit():
#             hasil *= int(reqem)
#     return hasil

# inputStr = input("Rəqəmləri daxil edin: ")
# print(reqemlerin_hasili(inputStr))

# 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın
# def bolenler(eded):
#     return [bolen for bolen in range(1, eded+1) if eded % bolen == 0]

# inputEded = int(input("Ədədi daxil edin: "))
# print(bolenler(inputEded))


# 5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.

# mənim listim
# mylist=['may','iyun','iyul']
# bu şəkildə olacaq
# {'may': 3, 'iyun': 4, 'iyul': 4}

# mylist = ['yanvar', 'fevral', 'mart', 'aprel', 'may', 'iyun', 'iyul', 'avqust', 'sentyabr', 'oktyabr', 'noyabr', 'dekabr']
# AylarUzunluqla = {ay: len(ay) for ay in mylist}
# print(AylarUzunluqla)


# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin (əlavə olaraq funksiya da 
# istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']

# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# adlar = [name.split()[0].lower() for name in names]
# print(adlar)


# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# results = [(nums1[i] + nums2[i]) / 2 for i in range(len(nums1))]
# print(results)












# listt = [1, 2, 3, 4, 5]
# print(list(filter(lambda x: x > 5, map(lambda x: x * 2, listt)))) 
