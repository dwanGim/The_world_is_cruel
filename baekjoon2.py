from collections import Counter

# #2753
# year = int(input())
# if 1 <= year <= 4000 :
#     if year%4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print("1")
#     else :
#         print("0")
# else : 
#     print("0부터 4000까지의 연도를 입력해주세요.")

# #2884
# H, M = map(int, input().split())

# M -= 45

# if M < 0 :
#     H -= 1
#     M += 60

# if H < 0 :
#     H += 24

# print(H, M)

# #2480

# dice = list(map(int, input().split()))
# diceCounter = Counter(dice)
# prize = 0


# if len(diceCounter) == 1 :
#     prize = 10000 + dice[0] * 1000
# elif len(diceCounter) == 2 :
#     for num, count in diceCounter.items() :
#         if count == 2 :
#             prize = 1000 + num * 100
# else :
#     prize = max(dice) * 100  

# print(prize)
