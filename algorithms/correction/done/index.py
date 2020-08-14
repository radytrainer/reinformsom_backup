# Monday
# Exercise 1
# text = str(input("Enter one word: ")) 
# countA = 0
# for n in range(len(text)):
#     if text[n] == "a" or text[n] == "A":
#         countA = countA + 1
# print("The number of A: ", countA)

#Exercise 2
# text = str(input("Enter one word: ")) 
# countA = 0
# message = ""
# for n in range(len(text)):
#     if text[n] == "a" or text[n] == "A":
#         countA = countA + 1
# if countA > 0:
#     message = "GOOD!"
# else:
#     message = "BAD!"
# print(message)

#Tuesday
#Exercise 1
# text = str(input("Enter one word: ")) 
# countA = 0
# countB = 0
# for n in range(len(text)):
#     if text[n] == "a" or text[n] == "A":
#         countA = countA + 1
#     if text[n] == "b" or text[n] == "B":
#         countB = countB + 1
# if countA == 2 and countB == 2:
#     print("WELL DONE!")
# else:
#     print("LOST!")

#Exercise 2

# text = str(input("Enter one word: ")) 
# countA = 0
# for n in range(len(text)):
#     if text[n] == "a" or text[n] == "A":
#         countA = countA + 1
# if countA == len(text):
#     print("WELL DONE!")
# else:
#     print("LOST!")

#Exercise 3
# text = str(input("Enter one word: ")) 
# countA = 0
# countB = 0
# for n in range(len(text)):
#     if text[n] == "a" or text[n] == "A":
#         countA = countA + 1
#     if text[n] == "b" or text[n] == "B":
#         countB = countB + 1
# if countA > countB:
#     print("WELL DONE!")
# else:
#     print("LOST!")

#Wednesday 
#Exercise 1
# wordOne = str(input("Word one: "))
# wordTwo = str(input("Word two: "))
# wordThree = str(input("Word three: "))
# sizeOne = len(wordOne)
# sizeTwo = len(wordTwo)
# sizeThree = len(wordThree)

# if sizeOne > sizeTwo and sizeOne > sizeThree:
#     print("The greatest character is: ", wordOne)
# elif sizeTwo > sizeOne and sizeTwo > sizeThree:
#     print("The greatest character is: ", wordTwo)
# elif sizeThree > sizeOne and sizeThree > sizeTwo:
#     print("The greatest character is: ", wordThree)
# else:
#     print("Two or 3 words are the same size")


# Exercise 2
# text = str(input("Enter one word: ")) 
# countChar = 0
# for n in range(len(text)):
#     if text[n] != " ":
#         countChar = countChar + 1
# print("The number of character: " ,countChar)

#Thursday 
#Exercise 1

# number = int(input("Enter one number: "))
# if number % 2 == 1:
#     print("This number is odd")
# else:
#     print("This number is even")

#Exercise 2
# maxNumber = int(input("Enter one number: "))
# sumEven = 0
# for n in range(maxNumber + 1):
#     if n % 2 == 0:
#         sumEven = sumEven + n
# print("Sum even number: ", sumEven)

#Friday
# Exercise 1
# numberOfValue = int(input("Enter number of value: "))
# countOdd = 0
# for n in range(numberOfValue):
#     number = int(input())
#     if number % 2 == 1:
#         countOdd = countOdd + 1
# print("Number of odd: ", countOdd)