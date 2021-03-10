while True:
    year = int(input("西暦何年？"))
    if (year%400 == 0) or ((year%4 == 0) and (year%100 != 0)):
        print("うるう年です")
    else:
        print("うるう年ではありません")
        
