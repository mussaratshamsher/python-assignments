
# # #write mode: opens the for writing
# # file = open("new_file.txt", "w")

# # # writing to files
# # file.write("Hello world!")
# # file.write(" \n New message")
# # file.close()
# # file = open("new_file.txt", "r")
# # content = file.read()
# # print(content)

# # line = file.readline()
# # print(line)
# # file.seek(0)
# # print("Position after seek(0):", file.tell())
# # lines = ["Line 1: Karachi\n", "Line 2: Lahore\n", "Line 3: Peshawar\n"]
# # content = file.read()
# # print(content)

# # file.seek(0)
# # lines = file.readlines()
# # for line in lines:
# #     print(line)

# # use with for automatic file cleanup
# # try:
# #     with open('unique.txt', 'x') as file:
# #         file.write("Created new file")
# #         print("File created successfully.")
# # except FileExistsError :
# #     print("File already exists.")       

# # with open("new_file.txt", "r") as file:
# #     content = file.read()
# #     print(content)
    
# with open("new_file.txt", "r") as file:
#     print(file.tell())

#     while True:
#         content = file.read(10)
#         if not content:
#             break
#         print(content)
#         i+= 1
import time
import datetime
ticks = time.time()
print("Time:", ticks)
t1 = time.localtime()
print( t1.tm_year)
print( t1.tm_mon)
print( t1.tm_mday)
print( t1.tm_hour)
print( t1.tm_min)
print( t1.tm_sec)
print( t1.tm_wday)
localtime = time.localtime(time.time())
print ("Local current time :", localtime)
print("Local current time :", time.asctime(localtime))
print("Current date and time:", datetime.datetime.now())
print("Current date:", datetime.date.today())
print("Current time:", datetime.datetime.now().time())
print("Current time:", datetime.datetime.now().strftime("%H:%M:%S"))
print("Current date:", datetime.datetime.now().strftime("%Y-%m-%d"))    


        