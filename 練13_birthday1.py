import datetime
# 生年月日を設定する

birthday1 = input("生年月日を入力してください(例:2017-04-01)　")
birthday2 = datetime.datetime.strptime(birthday1, '%Y-%m-%d')

print(type(birthday1), end="")
print(birthday1)
print(type(birthday2), end="")
print(birthday2)
