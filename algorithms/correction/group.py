studentScore = []
for i in range(3):
    score = int(input("Enter score: "))
    studentScore.append(score)
    studentScore.sort()
for n in range(len(studentScore)):
    print(studentScore[n], end= " , ")


