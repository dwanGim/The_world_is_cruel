# # 1316
# N = int(input())
# cnt = 0

# for _ in range(N):
#     word = input().lower()
#     is_group = True

# for i in range(len(word)-1):
#     if word[i] != word[i+1]:
#         if word[i+1:].count(word[i]) > 0:
#             is_group = False
#             break
    
#     if is_group:
#         cnt += 1

# if len(word) == 1:
#     cnt += 1

# print(cnt)

# # 2747

# n = int(input())

# def fibo(n):
#     x, y = 0, 1
#     for _ in range(n):
#         x, y = y, x+y
#     return x

# print(fibo(n))


# # 1316 다시 풀어보기
# # N = int(input())

# # words = []
# # cnt = 0


# # for _ in range(N):
# #     word = input().lower()
# #     words.append(word)

# # for word in words:
# #     isGroup = True
# #     prev = word[0]

# #     for char in word[1:]:
# #         if char != prev:
# #             if word.count(prev) > 1:
# #                 isGroup = False
# #                 break
# #             prev = char
# #     if isGroup:
# #         cnt+=1

# # print(cnt)

# N = int(input())

# words = []
# cnt = 0

# for _ in range(N):
#     word = input().lower()
#     words.append(word)

# for word in words:
#     isGroup = True
#     used_chars = set()
#     prev_char = None

#     for char in word:
#         if prev_char is None:
#             prev_char = char
#             used_chars.add(char)
#         else:
#             if char != prev_char and char in used_chars:
#                 isGroup = False
#                 break
#             prev_char = char
#             used_chars.add(char)

#     if isGroup:
#         cnt += 1

# print(cnt)

# # 14425
# N, M = map(int, input().split())

# S = set()
# list_M = []
# cnt = 0

# for _ in range(N):
#     S.add(input())

# for _ in range(M):
#     list_M.append(input())

# for i in list_M:
#     if i in S:
#         cnt +=1

# print(cnt)

# # 25083
# # 문제
# # 아래 예제와 같이 새싹을 출력하시오.

# # 입력
# # 입력은 없다.

# # 출력
# # 새싹을 출력한다.

# # 예제 입력 1 
# # 예제 출력 1 
# #          ,r'"7
# # r`-_   ,'  ,/
# #  \. ". L_r'
# #    `~\/
# #       |
# #       |


# print("         ,r'"+'"'+'7')
# print("r`-_   ,"+"'"+"  ,/")
# print(" \. "+'"'+". L_r'")
# print("   `~\\/")
# print("      |")
# print("      |")

# # 참고한 풀이
# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \. \". L_r'")
# print("   `~\/")
# print("      |")
# print("      |")

# # 3003

# data = {
#     'king' : 1,
#     'queen' : 1,
#     'rook' : 2,
#     'bishob' : 2,
#     'knight' : 2,
#     'pon' : 8
# }
# N = list(map(int, input().split()))
# data_val = list(data.values())
# result = [x-y for x, y in zip(data_val, N)]
# print(f'{str(result)[1:-1].replace(",","")}')

# # 1157
# N = input().upper()
# S = set()
# D = {}


# for char in N :
#      S.add(char)

# for char in S :
#     D[char] = N.count(char)

# L = list(D.values())
# max_cnt = max(L)
# max_char = [k for k, v in D.items() if v == max_cnt]

# if len(max_char) != 1:
#     print("?")
# else:
#     print(max_char[0])

# # 25206
# 너의 평점은...
# 인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!

# 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.

# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

data = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0,
    "P" : 0.0
}

name, score, char = map(str, input().split(' '))
# N, M = map(int, input().split())