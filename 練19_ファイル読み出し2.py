# coding: utf-8
# readの場合 (ファイルのEOFまで全て読み出す)
file1 = open("text.txt", mode="r")
str1 = file1.read()
file1.close()
print ("+"*50)
print ("readメソッドで読み込んだ場合の型 ⇒ ", end="")
print (type(str1))          #readで読み出したstr1には改行コードが含まれる
print (str1)
print ("")

# readline (1行ずつ文字列として読み出す)
file1 = open("text.txt", mode="r")
str1 = file1.readline()
print ("+"*50)
print ("readlineメソッドで読み込んだ場合の型 ⇒ ", end="")
print (type(str1))
while str1:                 #EOFまで読み出す
    print (str1, end="")    #readlineで読み出したstr1には改行コードが含まれる, 各printにも改行コードが付加されるためここではカットする
    str1 = file1.readline()
file1.close()
print ("")

# readlines (ファイルのEOFまで全て読み出し、配列に格納)
file1 = open("text.txt", mode="r")
str1 = file1.readlines()
file1.close()
print ("+"*50)
print ("readlinesメソッドで読み込んだ場合の型 ⇒ ", end="")
print (type(str1))          #1行ずつリストの要素に格納される
print ("普通に表示させた場合: ")
print (str1)
print ("\n(＊)ループを使ってリスト内の文字列表示させた場合: ")
for i in range(len(str1)):
    print (str1[i], end="") #リストの要素には改行コードも含まれるため、各printの改行コードはカットする
