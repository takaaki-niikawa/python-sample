score=[0]*10

print ("10人のテスト点数を入れて下さい")
for i in range(10):
    score[i] = input("?")

# テストの合計を求める
sum = 0
for i in score:
    sum += int(i)
    print (i, "点を足して合計は、", sum)

# 平均を求める
ave = sum / len(score)
print ("平均点は、", ave, "点です")
