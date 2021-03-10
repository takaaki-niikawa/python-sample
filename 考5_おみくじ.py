# おみくじ
from random import randint
while True:
    print("★★★ おみくじ ★★★")
    if int(input("9 以外の数字を入力してください:")) == 9:
        break

    kuji = randint(1, 3)
    if kuji == 1:
        print("大吉です。今週はラッキー！")
    elif kuji == 2:
        print("小吉です。がんばろー。")
    else:
        print("がびーん。凶です。今日は早めに寝よう。")
    print("")

print("おしまい")
