

# # for loop and string concatination
# for x in range(1,20,2):
#     print(x,"arsalan")

##while loop
# count = 5
# while count < 10:
#     print(count)
#     count +=1


# for loop with break points
# for x in range(20):
#     if x is 10:
#         print(x)
#         break
#     else:
#         print(x)

# print multiples of four
# for x in range(20):
#     if x is x%4:
#         print(x)

# continue
# number  = [2,5,12,14,15,6,17,8,9,20,22]
# for x in range(1,30):
#     if x in number:
#         continue
#         print("taken")


# functions
# def test(name):
#     print(name)
# test("arsalan")


#function return value
# def getage(age):
#     herage = age/2 + 7
#     return herage
#
# print(getage(39))

#default values
# def getgender(sex="unknown"):
#     if sex is "m":
#         print("male")
#     elif sex is "f":
#         print("female")
#     else:
#         print(sex)
# getgender("m")

#keywords
# def sentence(name="david", action="ate", item="chips"):
#     print(name, action, item)
#
# sentence(name="xubo")

#dynamic parameters or multiplr parameters

# def counter(*args):
#     total = 0
#     for a in args:
#        total += a
#        print(total)
# counter(1, 2, 3, 4, 5, 6, 7, 8, 9)

# #unpack arguments
# def calculator(amount, price, left):
#     print(amount, price, left)
# arguments = [11, 22, 33]
# calculator(*arguments)

# #sets
# sets = {"milk", "butter", "cheese", "milk"}
# print(sets)
#
# if "milk" in sets:
#     print("you already have it")
# else:
#     print("none")


#items

# classmates = {"alan":"page are left","james":"not so good","dean":"likes to walk"}
#
#
# for v, k in classmates.items():
#     print(v, k)


#modules

def tuna():
    print("its a fish")




