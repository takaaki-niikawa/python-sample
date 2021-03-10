# 1～100までの3の倍数か3の付く数字を表示する

for i in range(1, 101):
    if i % 3 == 0 or i % 10 ==  3 or (i >= 30 and i <= 39):
        print (i)
