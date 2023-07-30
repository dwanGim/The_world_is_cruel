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
