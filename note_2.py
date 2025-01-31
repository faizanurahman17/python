# name = "Faizanur Rahman"
# print(len(name))

# print(name[9:])

# String Functions

# str = "I am a coder."
# str.endswith("er.") #returns true if string ends with substr
# str. capitalize() #capitalizes 1st char
# str.replace( old, new)
# str.find( word) #returns 1st index of 1st occurrer
# str.count("am") #counts the occurrence of substr

# str = "my $ is $ for $ to $ in $"

# print("occurrence: ",str.count("$"))

# marks = float(input("enter your marks: "))

# if (marks >= 90):
#     print("grade = A")
# elif (90 > marks >= 80):
#     print("grade = B")
# elif (80 > marks >= 70):
#     print("grade = C")
# elif (70 > marks >= 50):
#     print("grade = D")
# elif (50 > marks >= 33):
#     print("grade = E")
# else :
#     print("Sorry You failed the exam")

#nesting

# haveLicence = input("Do you have a driving licence (yes/no): ").lower()

# if (haveLicence == "yes"):
#     age = int(input("enter your age: "))
#     if age >= 18:
#         licenseNum = input("enter your valid licence number: ")
#         if len(licenseNum) == 8 and licenseNum.endswith("ih"):
#             print("can drive")
#         else :
#             print("can't drive invalid licence number")
#     elif 16 <= age < 18:
#         licenseLNum = input("enter your valid learning licence number: ")
#         if len(licenseLNum) == 8:
#             print("can drive")
#         else :
#             print("can't drive (minor)\nor invalid learning licence number")
#     else :
#          print("can't drive")     
# else :
#     print("cannot drive")


# num = int(input("enter a number: "))

# if num % 2 == 0:
#     print("even number")
# else :
#     print("odd number")

# u,x,l = int(input("enter ur num: ")),int(input("enter ur num: ")),int(input("enter ur num: "))

# if x < u > l:
#     print("u is the greater of all nums ",u)
# elif x > l:
#     print("x is the greater of all nums ",x)
# else :
#     print("l is the greater of all nums ",l)

# num = int(input("enter a number: "))

# if num % 7 == 0:
#     print("yes the number is multiple of seven:",num)
# else:
#     print("not a multiple of seven:",num)