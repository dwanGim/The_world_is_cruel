from collections import Counter

# # 1330
# num1,num2 = map(int, input().split(" "))

# if num1 > num2:
#     print(f">")
# elif num1 < num2:
#     print(f"<")
# else:
#     print(f"==")

# #1008
# num1,num2 = map(int, input().split(" "))
# print(num1/num2)

# #10869
# A,B = map(int, input().split(" "))
# if A is not None and B is not None:
#     print(A+B)
#     print(A-B)
#     print(A*B)
#     print(A//B)
#     print(A%B)

#10926
# 준하는 사이트에 회원가입을 하다가 
# joonas라는 아이디가 이미 존재하는 것을 보고 놀랐다. 
# 준하는 놀람을 ??!로 표현한다. 
# 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 
# 주어졌을 때, 놀람을 표현하는 프로그램을 작성하시오.
# id_list = ["joonas", "baekjoon"]
# input_id = input()

# if input_id.isalpha():
#     if len(input_id) <=50:
#         if input_id in id_list:
#             print(input_id + "??!")

# # 답이 이거임 출제자 설명이 말도 안되는 것 같아요.
# print(input() + "??!")

# 18108
# year = int(input())
# print(year-543)

#10430
# A, B, C = map(int, input().split())

# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

# #10171 고양이
# print("\\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \\(__)|")

# #9408
# score = int(input())
# if 0 <= score <= 100 :
#     if score >= 90 :
#         print("A")
#     elif score >= 80 :
#         print("B")
#     elif score >= 70 :
#         print("C")
#     elif score >= 60 :
#         print("D")
#     else :
#         print("F")
# else :
#     print("0부터 100까지의 점수를 입력해주세요.")

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

# #2739
# gugu = int(input())

# for i in range(1, 10):
#     print(f"{gugu} * {i} = {gugu*i}")

# # 10950
# ran = int(input())
# for _ in range(ran):
#     A,B = map(int, input().split())
#     print(A+B)

# #8393
# n = int(input())
# total = 0
# for i in range(1, n+1):
#     total += i

# print(total)

# # 25304
# X = int(input())
# N = int(input())
# total = 0
# YN = "No"
# for _ in range(N) :
#     a,b = map(int, input().split())
#     total += a*b

# if total == X :
#     YN = "Yes"

# print(YN)

# # 25314
# N = int(input())
# longlong = N//4
# str = "long " * longlong
# print(str+"int")

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