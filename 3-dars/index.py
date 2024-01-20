
# my_list=[4,7,2,5,6,8,9,10,11,12,13,17,3,1]


# count=0
# def quick_sorted(list_a):
#     lenth=len(list_a)
#     global count


#     if lenth<2:
#         return list_a
    
#     else:
#         pivot=list_a.pop()
#         left_list=[]
#         right_list=[]
#         for i in list_a:
#             count=count+1
#             if pivot<i:
#                 right_list.append(i)
            
#             else:
#                 left_list.append(i)
#         return quick_sorted(left_list)+[pivot]+quick_sorted(right_list)


# print(quick_sorted(my_list),count)


# def buble_sorte(list_a):
#     index_length=len(list_a)-1
#     list_sorted=False
#     count=0
#     while not list_sorted:
#         list_sorted=True

#         for i in range(0,index_length):
#             count=count+1
#             if list_a[i]>list_a[i+1]:
#                 list_sorted=False
#                 list_a[i],list_a[i+1] =list_a[i+1],list_a[i]
#     return list_a , count



# print("Buble sorted",buble_sorte(my_list))



# def insertion_sorted(list_a):
#     length=len(list_a)
#     count=0

#     for i in range(1,length):
#         while list_a[i]<list_a[i-1] and i>0:
#             count=count+1
#             list_a[i],list_a[i-1]=list_a[i-1],list_a[i]
#             i=i-1
#     return my_list,count


# print("insertion sorted",insertion_sorted(my_list))