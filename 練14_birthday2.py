import datetime

# 生年月日をセットする
birthday1 = input("生年月日を入力してください(例:2017-04-01)　")
print(type(birthday1))
print(birthday1)

# 文字列から日付型に変換する
birthday2 = datetime.datetime.strptime(birthday1, '%Y-%m-%d')
print(type(birthday2))
print(birthday2)

# 今日の日付をセットする
today = datetime.datetime.now()
print(type(today))
print(today)

# 生年月日,今日の差分を計算
diff = today - birthday2

# 生まれた日の曜日を調べる
week = birthday2.strftime("%a")

print("")
print("あなたは、", birthday1, "に生まれて")
print(diff, "の間、生きています" )

print(birthday1, "の曜日は、", week, "でした")
