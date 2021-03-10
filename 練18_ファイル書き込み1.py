# テキストファイルを開く
file1 = open("test2.txt", mode="w")

# テキストを書く
file1.write("私は失敗したことがない\n")
file1.write("ただ、1万通りの、\n")
file1.write("うまく行かない方法を見つけただけだ。\n")

# テキストファイルを閉じる
file1.close()


