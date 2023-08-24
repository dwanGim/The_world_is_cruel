import sys

# # 2588
# num1 = int(input())
# if num1 <= 99 or num1 >= 1000:
#     print("세 자리 자연수를 입력해주세요.")
#     exit()
# num2 = int(input())
# if num2 <= 99 or num2 >= 1000:
#     print("세 자리 자연수를 입력해주세요.")
#     exit()

# result1 = num1 * (num2 % 10)
# result2 = num1 * ((num2 // 10) % 10)
# result3 = num1 * (num2 // 100)
# result4 = num1 * num2

# print(result1)
# print(result2)
# print(result3)
# print(result4)

# # 11382
# a, b, c = map(int, input().split())
# print(a+b+c)

# # 10172
# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')

# 10813
# N, M = map(int, input().split())
# baskets = [0] * N

# for _ in range(M):
#     i, j, k = map(int, input().split())
#     for idx in range(i-1, j):
#         baskets[idx] = k

# print(*baskets)

# 10813
N, M = map(int, input().split())
balls = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    balls[i-1], balls[j-1] = balls[j-1], balls[i-1]

print(*balls)
