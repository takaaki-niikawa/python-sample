# Ghost Game
from random import randint
print('ゆうれいゲーム')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 3)
    print('ドアが3つある。')
    print('そのうち1つのドアの向こうにゆうれいがいる。')
    print('さあ、何番のドアを開ける？')
    door = input('1、2、それとも3？')
    door_num = int(door)
    if door_num == ghost_door:
        print('ゆうれいだ！')
        feeling_brave = False
    else:
        print('ゆうれいはいなかった！')
        print('次の部屋に入れるよ。')
        score = score + 1
print('逃げろ！')
print('ゲームオーバー！　スコアは',score,'です。')
