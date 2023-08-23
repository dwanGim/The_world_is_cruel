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


# # 10818
# len(배열) 메서드는 배열의 길이를 가르쳐줍니다.
# min(배열)과 max(배열)을 통해 최솟값과 최댓값을 구할 수 있습니다.
# N = int(input())
# nums = list(map(int, input().split()))

# if N == len(nums):
#     print(f"{min(nums)} {max(nums)}")
# else:
#     print("첫번째로 주어진 N과 동일한 길이의 배열을 제공해주세요!")

# # 2562
# max(배열) 메서드는 배열의 최댓값을 찾아줍니다.
# 배열.index(인덱스) 메서드는 배열 내부에서 인덱스의 위치를 찾아줍니다. 
# nums = []
# roop = 9
# for i in range(0, roop):
#     N = int(input())
#     nums.append(N)

# max_num = max(nums)
# print(max_num)
# print(nums.index(max_num)+1)

# 10810
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다. 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.

# 도현이는 앞으로 M번 공을 넣으려고 한다. 도현이는 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다. 만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다. 공을 넣을 바구니는 연속되어 있어야 한다.

# 공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.
