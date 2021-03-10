if int(input("1:パスワード初期化、2:パスワードチャレンジのどちらかを入力してください: ")) == 1:
    print("パスワードを初期化します...")
    with open("pw.txt", "w") as f:
        string1 = input("5桁の数字を入力してください: ")
        f.write(string1)
else:
    print("パスワードにチャレンジしていただきます...")
    with open("pw.txt", "r") as f:
        string1 = f.read()
        if int(input("5桁の数字を入力してください: ")) == int(string1):
            print("パスワードは正しいです。解除に成功しました！")
        else:
            print("パスワードは間違っています")
