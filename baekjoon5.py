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

# # 10813
# N, M = map(int, input().split())
# balls = list(range(1, N+1))

# for _ in range(M):
#     i, j = map(int, input().split())
#     balls[i-1], balls[j-1] = balls[j-1], balls[i-1]

# print(*balls)

# # 5597
# students = set()
# for _ in range(28):
#     n = int(input())
#     students.add(n)

# nums = set(range(1,31))
# result = nums.difference(students)
# print(min(result))
# print(max(result))

# # 3052
# # set은 중복되지 않은 값들의 집합을 나타내며
# # 배열의 원소들을 set으로 변환하여 중복되지 않은 값들만 남습니다.
# # 이후 set의 길이를 확인하면 서로 다른 값의 개수를 얻을 수 있습니다.
# n = []
# for _ in range(10):
#     x = int(input())
#     n.append(x%42)

# cnt = len(set(n))
# print(cnt)

# # 27866
# S = input()
# i = int(input())
# print(S[i-1])

# # 2743
# word = input()
# print(len(word))

# # 9086
# T = int(input())
# for _ in range(T) :
#     word = input()
#     print(word[0]+word[len(word)-1])

# # 11654
# # 파이썬 라이브러리의 ord를 사용해 아스키코드 출력
# str = input()
# ascii = ord(str)
# print(ascii)

# # 11720
# N = int(input())

# numbers = input()
# total = sum(int(digit) for digit in numbers)
# print(total)

# # 10809
# # 알파벳 소문자 개수만큼 -1로 초기화된 리스트를 생성합니다.
# result = [-1] * 26
# # 입력 문자열을 받습니다.
# word = input()
# # 입력 문자열을 순회하면서 각 알파벳의 위치를 업데이트합니다.
# for i in range(len(word)):
#     # 알파벳의 아스키 코드 값을 이용해서 해당 알파벳이 처음 등장하는 위치를 저장합니다.
#     index = ord(word[i]) - ord('a')
#     if result[index] == -1:
#         result[index] = i

# # 결과 리스트를 공백으로 구분하여 출력합니다.
# print(" ".join(map(str, result)))

# # 2908
# # 두 개의 수를 입력받습니다.
# A, B = map(int, input().split())

# # 두 수를 거꾸로 읽은 값을 구합니다.
# A = int(str(A)[::-1])
# B = int(str(B)[::-1])

# # 더 큰 값을 출력합니다.
# print(max(A, B))

# # 2675
# # 테스트 케이스의 개수 T 입력
# T = int(input())

# # 각 테스트 케이스에 대해 반복
# for _ in range(T):
#     # 반복 횟수 R과 문자열 S 입력
#     R, S = input().split()
    
#     # 문자열 S의 각 문자를 R번 반복하여 P를 만듦
#     P = ''.join([char * int(R) for char in S])
    
#     # 결과 출력
#     print(P)

# # 2444 별찍기
# N = int(input())

# # 위쪽 삼각형 출력
# for i in range(1, N + 1):
#     spaces = " " * (N - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)

# # 아래쪽 삼각형 출력
# for i in range(N - 1, 0, -1):
#     spaces = " " * (N - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)

# # 10988
# n = input()

# # 문자열을 뒤집은 것과 원래 문자열이 같으면 팰린드롬
# if n == n[::-1] : print(1) 
# else : print(0)



# # 2720
# T = int(input())
# for _ in range(T):
#     C = int(input()) / 100

#     quarters = int(C / 0.25)
#     C %= 0.25
    
#     dimes = int(C / 0.10)
#     C %= 0.10
    
#     nickels = int(C / 0.05)
#     C %= 0.05
    
#     pennies = int(C / 0.01)

#     print(quarters, dimes, nickels, pennies)


# # 1152
# s = input()
# strip_s = s.strip()
# # print(strip_s)
# result = len(strip_s.split())
# print(result)

# # # 5622

# dial = {
#     'A': 3, 'B': 3, 'C': 3,
#     'D': 4, 'E': 4, 'F': 4,
#     'G': 5, 'H': 5, 'I': 5,
#     'J': 6, 'K': 6, 'L': 6,
#     'M': 7, 'N': 7, 'O': 7,
#     'P': 8, 'Q': 8, 'R': 8, 'S': 8,
#     'T': 9, 'U': 9, 'V': 9,
#     'W': 10, 'X': 10, 'Y': 10, 'Z': 10
# }

# s = (input()).upper()
# time = 0

# for i in s:
#     time += dial[i]

# print(time)

# # 2941

# data = {
#     'c=': 'č',
#     'c-':'ć',
#     'dz=':'dž',
#     'd-':'đ',
#     'lj':'lj',
#     'nj': 'nj',
#     's=': 'š',
#     'z=': 'ž'
# }
# print(data)
# croatians = list(data.keys())

# s = input()
# result = []
# i = 0

# while i < len(s):
#     found = False
#     for croatian in croatians:
#         if s[i:].startswith(croatian):
#             result.append(croatian)
#             i += len(croatian)
#             found = True
#             break
#     if not found:
#         result.append(s[i])
#         i += 1

# print(len(result))

# # 1546
# N = int(input())
# scores = list(map(int, input().split()))

# max_score = max(scores)

# new_scores = [score / max_score * 100 for score in scores]

# avr = sum(new_scores) / N

# print(avr)

# 10811
N, M = map(int, input().split())

baskets = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i - 1:j] = reversed(baskets[i - 1:j])


print(' '.join(map(str, baskets)))