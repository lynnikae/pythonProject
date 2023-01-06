f = open("24_6.txt")
s = f.readline()
isnumber = []
for i in range(len(s)):
    if s[i] == "8" and s[i + 1].isdigit() and s[i + 2].isdigit() and s[i + 3].isdigit() and s[i + 4].isdigit() and s[
        i + 5].isdigit() and s[i + 6].isdigit() and s[i + 7].isdigit() and s[i + 8].isdigit() and s[i + 9].isdigit() and \
            s[i + 10].isdigit() and s[i + 11].isalpha() and (int(s[i + 9]) + int(s[i + 10]) % 2 == 0):
        isnumber.append(
            s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] + s[i + 5] + s[i + 6] + s[i + 7] + s[i + 8] + s[i + 9] + s[
                i + 10])
print(isnumber)