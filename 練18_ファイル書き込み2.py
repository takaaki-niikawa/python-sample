file1 = open("test2.txt", mode="w")

try:
    file1.write("私は失敗したことがない\n")
    file1.write("ただ、1万通りの、\n")
    file1.write("うまく行かない方法を見つけただけだ。\n")
    print("ファイルに書き込みました。")
except:
    print("エラーが発生しました。")
finally:
    print("ファイルを閉じます...")
    file1.close()

