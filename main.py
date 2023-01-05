# f = open('3.txt')
# s = f.readline().split("Y")
# max_len = 0
# for i in range(len(s)-1):
#     if len(s[i] + "Y" + s[i + 1]) > max_len:
#         max_len = len(s[i] + "Y" + s[i + 1])
# print(max_len)

# f = open('5.txt')
# s = f.readline().replace("CDK", "CD_DK").replace("CD", "0").replace("DK", "0")
# for i in range(1, 100):
#     if '0' * i in s:
#         print(i)


# f = open('6.txt')
# s = f.readline().replace("E", "A").replace("C", "B").replace("D", "B")
# for i in range(1, 100):
#     if "BA" * i in s:
#         print(i)


# f = open('1.txt')
# s = f.readline().split("XXZY")
# print(len(max(s, key=len)))
# print(s.index(max(s, key=len)))
# print(len(s))
# ИЛИ
# s = f.readline().replace("XXZY", "XXZ XZY").split()
# print(len(max(s, key=len)))


# f = open('2.txt')
# s = f.readline().split("E")
# maxx = 0
# for i in s:
#     if i.count("A") >= 3 and len(i) > maxx:
#         maxx = len(i)
# print(maxx)


# f = open('3.txt')
# s = f.readline().split("E")
# cnt = 0
# for i in s:
#     if "Z" not in i and len(i) >= 12:
#         cnt += 1
# print(cnt)


# f = open('4.txt')
# cnt = 0
# for s in f:
#     if s.count("AB") > 1 and s.count("C") > 1 and s.count("AB") >= s.count("C"):
#         cnt += 1
# print(cnt)


# f = open('5.txt')
# cnt = 0
# for s in f:
#     if s.count("A") == 4 and s.count("Y") >= 3:
#         cnt += 1
# print(cnt)

# f = open('6.txt')
# # s = f.readline().replace("B", "F").replace("C", "F").replace("D", "F").replace("E", "F")
# # print(s.count("FAA"))
# #ИЛИ
# s = f.readline()
# cnt = 0
# for i in range(len(s) - 2):
#     if s[i] != s[i + 2] and s[i + 1] in "FCA" and s[i + 1] == s[i + 2] and s[i + 2] in "ABE":
#         cnt += 1
# print(cnt)


# f = open("7.txt")
# s = f.readline()
# cnt_kl, lens = 0, []
# for i in range(len(s) - 1):
#     if cnt_kl < 21 and s[i] == "K" and s[i + 1] == "L":
#         cnt_kl += 1
#     if cnt_kl == 21 and s[i] == "K" and s[i + 1] == "L":
#         lens.append(i + 1 - s.index("KL") + 1)
#         s = s.replace("KL", "00", 1)
# print(min(lens))









