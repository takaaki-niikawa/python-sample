# あるクラスの国語テストの点数をリストに代入
score = [88, 76, 67, 43, 79, 80, 91]

# テストの合計を求める
sum = 0
for i in score:
    sum += i
    print (i, "点を足して合計は、", sum)

# 平均を求める
ave = sum / len(score)
print ("平均点は、", ave, "点です")
