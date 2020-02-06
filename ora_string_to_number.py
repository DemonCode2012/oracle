s = input("输入要转换的英文和字母")
s = s[:15]
print(s)

ls = list(s)
sum = 0
for i in range(len(ls)):
    # print(ls[i])
    sum += pow(256, 15 - i) * ord(ls[i])
    # print(pow(256, 15 - i))
    # print(sum)
print("转换后的数字为：", int(str(sum)[:21]))