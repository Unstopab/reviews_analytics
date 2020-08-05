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