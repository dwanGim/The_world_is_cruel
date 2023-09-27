# # 17680
# from collections import deque

# def solution(cacheSize, cities):
#     cache = deque([], maxlen=cacheSize)
#     time = 0
#     for city in cities:
#         city = city.lower()
#         if city in cache:
#             cache.remove(city)
#             cache.append(city)
#             time += 1
#         else:
#             cache.append(city)
#             time += 5
#     return time

# # 120956
# def solution(babbling):
#     answer = 0
#     words = ['aya', 'ye', 'woo', 'ma']

#     for babble in babbling:
#         for word in words:
#             if word + word in babble:
#                 continue
#             else:
#                 babble = babble.replace(word, "")
#         if babble:
#             continue
#         else:
#             answer += 1

#     return answer

# # 120835
# def solution(emergency):
#     answer = []
#     chart = emergency.copy()
#     chart.sort(reverse = True)

#     for i in emergency:
#         answer.append(chart.index(i) + 1)
#     return answer
