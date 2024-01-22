# class MYIterator:


#     def __init__(self,data):
#         self.data=data
#         self.index=0


#     def __iter__(self):
#         return self
    


#     def __next__(self):
#         if self.index<len(self.data):
#             rezult=self.data[self.index]
#             self.index+=1

#         else:
#             raise StopIteration
        


# my_list=[1,2,3,4,5,6]
# data=MYIterator(my_list)


# print(my_list.__dir__())
        



# def square(num):
#     return num**2



# my_ist=[1,2,3,4,5,6]

# res=(map(square,my_ist))


# print(res)

# for i in res:
#     print(i)





# import random
# import time


# names=["Abdulaziz","Murodjon","Hasanboy","Ilyosbek","Asrorbek","Yahyobek","Farruxbek"]

# majors=["It","Filalogiya","Tarix","Jismoniy tarbiya","Iqtisod","Meditsina","Boshlangizch"]


# def people(people_num):
#     rezult=[]


#     for i in range(people_num):
#         person={
#             "id":i,
#             "name":random.choice(names),
#             "majors":random.choice(majors)
#         }
#         rezult.append(person)

#     return rezult


# time1=time.time()
# people1=people(100000000)
# time2=time.time()

# print(people1)





# import random
# import time


# names=["Abdulaziz","Murodjon","Hasanboy","Ilyosbek","Asrorbek","Yahyobek","Farruxbek"]

# majors=["It","Filalogiya","Tarix","Jismoniy tarbiya","Iqtisod","Meditsina","Boshlangizch"]


# def people(people_num):
#     rezult=[]


#     for i in range(people_num):
#         person={
#             "id":i,
#             "name":random.choice(names),
#             "majors":random.choice(majors)
#         }
#         rezult.append(person)

#     return rezult
# def people_generator(people_num):
#     for i in range(people_num):

# time1=time.time()
# people1=people(100000000)
# time2=time.time()

# print(time2-time1)










# import random
# import time

# name=["Asadbek", "Murodjon", "Hasanbor" , "Ilyosbek" , "Yaxyobek" , "Abdulaziz" , "Farruxbek"]

# majors=["IT", "Filologiya", "Tarix", "Jidmoniy tarbiya", "iqtisof", "Med", "boshlangich"]

# def people_list(people_num):
#     result= []
#     for i in range(people_num):
#         person={
#             "id":i,
#             "name":random.choice(name),
#             "majors":random.choice(majors)}
#         result.append(person)
#     return result

# def people_generator(people_num):
#     result= []
#     for i in range(people_num):
#         person={
#             "id":i,
#             "name":random.choice(name),
#             "majors":random.choice(majors)}
#         result.append(person)
#     yield result

# time1=time.time()
# people=people_generator(1000000)
# time2=time.time()



# print(people)