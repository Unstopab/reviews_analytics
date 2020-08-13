data =[]
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        if len(data) % 1000 == 0:
            print(len(data))
print("檔案讀取完了，總共有", len(data), "筆資料")

sum_len = 0
for d in data:
    sum_len += len(d)
print("其中檔案總共有", sum_len, "個字")
print("平均留言長度為", sum_len/len(data), "字")

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("\n一共有", len(new), "筆資料留言字數小於100")

good = []
for d in data:
    if "good" in d:
        good.append(d)
print("而在留言中有提到'good'一詞的共有", len(good), "筆")

#文字計數
wc = {} #word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增新的key進wc字典

for word in wc: #每個word就是字典裡的每一個key
    if wc[word] >1000000:
        print(word,wc[word])

print(len(wc))

while True:
    word = input("請問你想查什麼字?")
    if word == "q":
        break 
    elif word in wc:
        print(word, "在這份文件中出現過", wc[word], "次")
    else:
    	print("這個字沒有出現過哦")

print("感謝使用本查詢功能")





