# f = open("1.txt")
# s = f.readline()
# bukvy = {}
# for i in range(len(s)-1):
#     if s[i + 1] == "Z":
#         if s[i] in bukvy:
#             bukvy[s[i]] += 1
#         else:
#             bukvy[s[i]] = 1
# print(max(bukvy, key=bukvy.get))
# print(bukvy["Q"])
# print(bukvy)
from pprint import pprint

# f = open('2.txt')
# s = f.readline()
# bukvy = {}
# for i in range(len(s) - 2):
#     if s[i] == "D" and s[i + 2] == "P":
#         if s[i + 1] in bukvy:
#             bukvy[s[i + 1]] += 1
#         else:
#             bukvy[s[i + 1]] = 1
# print(max(bukvy, key=bukvy.get))
# print(bukvy["I"])
# print(bukvy)



# f = open("4.txt")
# maxdist = 0
# for s in f:
#     if s.count("a") < 20:
#         for bukva in s:
#             maxdist = max(maxdist, s.rindex(bukva) - s.index(bukva))
# print(maxdist)




# f = open("5.txt")
# minB = "B" * 1000000000
# for s in f:
#     if s.count("B") <= minB.count("B"):
#         minB = s
# for bukva in "QWERTYUIOPASDFGHJKLZXCVBNM":
#     print(bukva, minB.count(bukva))



# f = open("6.txt")
# s = f.readline()
# cnt = 0
# for i in range(len(s)):
#     if s[i:i+7] == s[i:i+7][::-1]:
#         cnt += 1
# print(cnt)