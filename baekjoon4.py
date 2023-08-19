import sys
 
##15552
# inp = int(input())
# for i in range(inp):
#         a,b = map(int, sys.stdin.readline().split())
#         print(a+b)

# #11021
# N = int(input())
# for i in range(1, N+1):
#     A,B=map(int, input().split())
#     print(f"Case #{i}:{A+B}")

# # 11022
# # 두 정수 A와 B를 입력받은 다음, A+B를 출력한다.
# # 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# # 각 테스트 케이스마다 "Cass #x: A + B = C"형식으로 출력한다.
# T = int(input())
# for i in range(1, T+1):
#     A,B=map(int, input().split())
#     print(f"Case #{i}: {A} + {B} = {A+B}")

# # 2438
# # 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# # 첫째 주루터 N번째 줄까지 차례대로 별을 출력한다.
# #  **파이썬의 개행문자는 \n입니다.**
# #  개행문자 쓸 필요가 없었네요..
# T = int(input())
# for i in range(1, T+1):
#     print("*"*i)

# # # 2439
# # # 오른쪽 기준으로 정렬한 별을 출력해보세요.
# T = int(input())
# for i in range(1, T+1):
#     spaces = " " * (T-i)
#     stars = "*"*i
#     print(spaces+stars)

# # 10952
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     else:
#         print(a+b)

# # 10951
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

# # 10807
# N = int(input())
# num_list = list(map(int, input().split()))
# v = int(input())

# cnt = 0
# for i in num_list:
#     if i == v:
#         cnt += 1
# print(cnt)