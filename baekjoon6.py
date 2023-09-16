# 1316
N = int(input())
cnt = 0

for _ in range(N):
    word = input().lower()
    is_group = True

for i in range(len(word)-1):
    if word[i] != word[i+1]:
        if word[i+1:].count(word[i]) > 0:
            is_group = False
            break
    
    if is_group:
        cnt += 1

if len(word) == 1:
    cnt += 1

print(cnt)