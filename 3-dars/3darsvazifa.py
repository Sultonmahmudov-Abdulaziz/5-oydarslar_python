



# 2-misol


# def index(raqam):
  
#     teskari_raqam = int(str(raqam)[::-1])
    
#     return teskari_raqam == raqam


# natija = index(121)

# print("Javob:", natija)


# 3-misol

# def eng_kop_takrorlanayotgan(matn):
#     char_tur = {}
#     takor_element = ''
#     takror_son = 0

#     for element in matn:
#         if element.isalnum():  
#             element = element.lower() 
#             if element in char_tur:
#                 char_tur[element] += 1
#                 if char_tur[element] > takror_son:
#                     takror_son= char_tur[element]
#                     takor_element = element
#             else:
#                 char_tur[element] = 1

#     return f'"{takor_element}" {takror_son} marta eng ko\'p takrorlangan'


# matn = "fiolgpwogjeol4efhu4ofilhcf43k9wigh43aiaopi4hw233"
# natija = eng_kop_takrorlanayotgan(matn)

# print("Javob:", natija)




# 4-misol 


# def tekshir_qavs(matn):
#     qavs_turlari = {"(": ")", "{": "}", "[": "]"}
#     sahifa = []

#     for simvol in matn:
#         if simvol in qavs_turlari.keys():
#             sahifa.append(simvol)
#         elif simvol in qavs_turlari.values():
#             if not sahifa or qavs_turlari[sahifa.pop()] != simvol:
#                 return False  

#     return not sahifa  


# matn = "[euwfygwyfuy]"
# if tekshir_qavs(matn):
#     print(f"Matnda {matn} shartda kiritilgan qavslar yopilgan")
# else:
#     print(f"Matnda {matn} shartda kiritilgan qavslar  yopilmagan")


# 5-misol


# def topish_index(element, royxat):
#     for i, el in enumerate(royxat):
#         if el == element:
#             return i
#     return -1  


# royxat = [10, 20, 30, 40, 50]
# element = 30

# indeks = topish_index(element, royxat)
# if indeks != -1:
#     print(f"{element} element {indeks}-indexda joylashgan.")
# else:
#     print(f"{element} elementi ro'yxatda topilmadi.")



# 6-misol


# def insertion_sort(royxat):
#     for i in range(1, len(royxat)):
#         key = royxat[i]
#         j = i-1
#         while j >= 0 and key > royxat[j]:
#             royxat[j+1] = royxat[j]
#             j -= 1
#         royxat[j+1] = key


# my_list= [64, 34, 25, 12, 22, 11, 90]
# print("Boshlang'ich ro'yxat:", my_list)

# insertion_sort(my_list)
# print("Teskari sorted ro'yxat:", my_list)






