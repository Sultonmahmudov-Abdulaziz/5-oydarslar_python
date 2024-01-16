# 1-misol


# def sonlar(raqamlar):
#     n = len(raqamlar)

#     for i in range(n):
#         for j in range(0, n-i-1):
#             if raqamlar[j] > raqamlar[j+1]:
               
#                 raqamlar[j], raqamlar[j+1] = raqamlar[j+1], raqamlar[j]

#     return raqamlar

# my_list= [4, 2, 7, 1, 9, 3]
# tartiblangan=sonlar(my_list)
# print(tartiblangan)



# 2-misol


# def teskari(matn):
#     return matn[::-1]

# tex = "Salom, dunyo!"
# natija = teskari(tex)
# print(natija)


# 3-misol


# def num(fayl_nomi):
#     try:
#         with open(fayl_nomi, 'w', encoding='utf-8') as fayl:
#             fayl.write("Siz dasturlashni yangi boshlaysizmi yoki tajribali dasturchi bo'lasizmi, Pythonni o'rganish va undan foydalanish oson.")

#         with open(fayl_nomi, 'r', encoding='utf-8') as fayl:
#             matn = fayl.read()
#             sozlar = matn.split()
#             return len(sozlar)
#     except Exception as e:
#         return f"Xatolik: {e}"

# fayl_nomi = 'python.txt'
# natija = num(fayl_nomi)

# print(f"So'zlarni soni: {natija}")



# 4-misol

# ishlay olmadim oziz ishlab tushuntrib bersez yahshi bolardi


# 5-misol


# def binary_search(target, lower_limit, upper_limit):
#     attempts = 0
    
#     while lower_limit <= upper_limit:
#         middle = (lower_limit + upper_limit) // 2
#         attempts += 1

#         print(f"Urinish #{attempts}: Foydalanuvchi {middle} sonini taxmin qildi.")

#         if middle == target:
#             return middle, attempts
#         elif middle < target:
#             lower_limit = middle + 1
#             print(f"Juda past! .")
#         else:
#             upper_limit = middle - 1
#             print(f"Juda yuqori! .")
    
#     return None, attempts


# foydalanuvchi_tanlangan_son = int(input("Foydalanuvchi sonni kiriting (1-50 oraliq): "))

# past_limit = 1
# upper_limit = 50

# tanlangan_son, urinishlar_soni = binary_search(foydalanuvchi_tanlangan_son, past_limit, upper_limit)

# if tanlangan_son is not None:
#     print(f"Foydalanuvchi {tanlangan_son} sonini to'g'ri topdi.")
#     print(f"Umumiy urinishlar soni: {urinishlar_soni}")
# else:
#     print("Foydalanuvchi tanlagan son topilmadi.")
