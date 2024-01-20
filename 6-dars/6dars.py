# 1-misol


# 2-misol

# def unli_element(sozlar):
#     eng_katta_unli = ''
#     unli_son = 0

#     for soz in sozlar:
#         unli_harf_soni = sum(1 for harf in soz if harf.lower() in 'aeiou')
#         if unli_harf_soni > unli_son:
#             eng_katta_unli = soz
#             unli_son = unli_harf_soni

#     return eng_katta_unli, unli_son

# # Test qilish
# sozlar = ["apple", "banana","Abdulaziz", "kiwi", "grapefruit"]
# natija_soz, unli_son = unli_element(sozlar)
# print(f"Berilgan so'zlar: {sozlar}")
# print(f"Eng katta unli qatnashgan soz: {natija_soz}")
# print(f"Unlilar soni: {unli_son}")



# 3-misol


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key > arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key


# arr = [64, 95, 12, 89, 11]
# insertion_sort(arr)

# print("Tartiblangan ro'yxat:", arr)



# 4-misol

def count_words(text):
    words = text.split(" ")
    
    words = [word for word in words if word]
    return len(words)

matn = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a
galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap 
into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
soni = count_words(matn)
print(soni)



# 5-misol

# def format_text(input_text):
#     words = input_text.split()
#     hashtag = "#"
    
#     if not words:
#         return False
#     words = [word.capitalize() for word in words]
    
#     hashtag += ''.join(words)
    
    
#     if len(hashtag) > 140:
#         return False
    
#     return hashtag


# misol= "hello world "

# natija=format_text(misol)
# print(natija)

