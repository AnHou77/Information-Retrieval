N = int(input())
final_score = 0.0
for i in range(N):
    querys = input().split()
    relavents = input().split()
    score = 0.0
    cnt = 0.0
    for j in range(len(querys)):
        if querys[j] in relavents:
            cnt += 1
            score += (cnt / (j + 1))
    final_score += (score / len(relavents))
print(round(final_score / N, 4))