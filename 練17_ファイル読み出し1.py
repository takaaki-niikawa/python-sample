# テキストファイルを開く
file1 = open("test1.txt", mode="r")

# テキストを読む
string = file1.read()

# テキストファイルを閉じる
file1.close()

# 結果を表示する
print(string)

