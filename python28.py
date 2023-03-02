# writing and appending to a file..........
# f=open("riya.txt","w")
# a=f.write("i am a good girl")
# print(a)
# f.close()

# handle read and write both
# f=open("riya.txt","r+")
# print(f.read())
# f.write("thank you")

# pattern printing

# seek(),tell(),more on python file.......

# f=open("riya.txt")
# print(f.tell())
# print(f.readline())
# f.seek(10)
# f.close()

# using with block to open python files....
# with open("riya.txt") as f:
#    a=f.read(4)
#    print(a)

# health management system:
# 3 clients - Harry, Rohan and Hammad
def getdate():
    import datetime
    return datetime.datetime.now()
