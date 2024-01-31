import asyncio




async def main():
    print("I am Running...1")


async def main():
    asyncio.sleep(5)
    print("I am Running ...2")

async def main():
    await asyncio.sleep(3)
    print("I am Running ...3")

async def main():
    print("I am Running...4")


async def main1():
    task1 = asyncio.create_task(main())
    task2 = asyncio.create_task(main())
    task3 = asyncio.create_task(main())
    task4 = asyncio.create_task(main())


    await task1
    await task2 
    await task3
    await task4


asyncio.run(main1())



# import time


# start=time.perf_counter()
# async def main(secs):
#     await asyncio.sleep(secs)
#     print(f"Running {secs}")
          
          
          
# async def main1():
#     async with asyncio.TaskGroup() as tg:
#         for i in range(6):
#             tg.create_task(main(i))


# asyncio.run(main1())
# finish=time.perf_counter()
# print(f" Running in >> { round ( finish-start,2)}")


# import time
# import os


# def clock():
#     start_time=round(time.time())
#     while True:
#         if(round(time.time())-start_time)%5==0:  
#             yield '5 seconds'
#         else: 
#             yield 0


# def query():
#     for i in os.walk('C:\\'):
#         yield i[0]


# def main():
#     data=query()
#     alarm=clock()

#     while True:
#         d=next(data)
#         a=next(alarm)
#         print(d)
#         if a:print(a)
#         time.sleep(1)

# main()
