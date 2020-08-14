# Monday
# Exercise 1
# text = str(input("Ente one word: "))
# countA = 0
# for n in range(len(text)):
#     if text[n] == "a" or text[n] == "A":
#         countA = countA + 1
# print("Number of A: " + str(countA))

# Exercise 2
# text = str(input("Ente one word: "))
# result = ""
# countA = 0
# for n in range(len(text)):
#     if text[n] == "a" or text[n] == "A":
#         countA = countA + 1
#     if countA > 0:
#           result = "GOOD!"
#     else:
#         result = "BAD!"
# print(result)
        
#Tuesday
# Exercise 1
# text = str(input("Ente one word: "))
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
# text = str(input("Ente one word: "))
# countainAOnly = 0
# for n in range(len(text)):
#     if text[n] == "a" or text[n] == "A":
#         countainAOnly = countainAOnly + 1
# if countainAOnly == len(text):
#     print("WELL DONE!")
# else:
#     print("LOST!")

#Exercise 3
# text = str(input("Ente one word: "))
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
# wordOne = str(input("Enter word one: "))
# wordTwo = str(input("Enter word two: "))
# wordThree = str(input("Enter word three: "))
# wordOneSize = len(wordOne)
# wordTwoSize = len(wordTwo)
# wordThreeSize = len(wordThree)

# if wordOneSize > wordTwoSize and wordOneSize > wordThreeSize:
#     print("The greatest word is: " , wordOne)
# elif wordTwoSize > wordOneSize and wordTwoSize > wordThreeSize:
#     print("The greatest word is: ", wordTwo)
# elif wordThreeSize > wordOneSize and wordThreeSize > wordTwoSize:
#     print("The greatest word is: ", wordThree)
# else:
#     print("Two or 3 words are the same size")

#Exercise 2
# text = str(input("Enter one word: "))
# countChar = 0
# for n in range(len(text)):
#     if text[n] != " ":
#         countChar = countChar + 1
# print("The number of letters is:", countChar)

#Thursday
#Exercise 1

# number = int(input("Enter one number: "))
# if number % 2 == 1:
#     print("this number is odd")
# else:
#     print("this number is even")

#Exercise 2
# number = int(input("Enter one number: "))
# sumEven = 0
# for n in range(number + 1):
#     if n % 2 == 0:
#         sumEven = sumEven + n 
# print(sumEven)

#Friday
#Exercise 1

numberOfValue = int(input("Number of values: "))
countOdd = 0
for n in range(numberOfValue):
    number = int(input())
    if number % 2 == 1:
        countOdd = countOdd + 1
print("---------------------------")
print("Number of Odd: " ,countOdd)