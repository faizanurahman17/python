# Loops

# while loops

# while contition :
    # some work


# i = 1 # itarator
# while i <= 5 : #stopping condition
#     print("hello world",i)
#     i += 1 #itaration

# print("loop changed",1)

# i = 1
# while i <= 5 :
#     print("*",i)
#     i += 1

# print("loop changed",2)

# i = 5
# while i >= 1 :
#     print("*",i)
#     i -= 1


# practice

# print numbers from 1 - 100 & opposite

# i = 1
# while i <= 100 :
#     print("*",i)
#     i += 1

# print("--------")

# i = 100
# while i >= 1 :
#     print("*",i)
#     i -= 1

# multiplication table of number n

# i = 1
# n = int(input("enter any natural number: "))
# while  i <= 10:
#     print(n,"x",i,"=",n * i)
#     i += 1

# Print the elements of the following list using a loop:
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# print(len(list))

# i = 0
# while i < len(list) :
#     print(list[i])
#     i += 1

list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("enter a num to search: "))
i = 0
while i < len(list) :
    if list[i] == x :
        print("found at idx", i)
    i += 1