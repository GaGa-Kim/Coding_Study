score1 = int(input())
score2 = int(input())
score3 = int(input())
score4 = int(input())
score5 = int(input())
scores = [score1, score2, score3, score4, score5]

for i in range(len(scores)):
    if scores[i] <= 40:
        scores[i] = 40
result = sum(scores)
print(result//5)

