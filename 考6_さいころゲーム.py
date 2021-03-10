# さいころゲーム
from random import randint
print("Let's start さいころゲーム!!")

a = 0
while a!='x':
    a=input("Please hit 'x': ")
    x = randint(1, 6)
while a!='y':
    a=input("Please hit 'y': ")
    y = randint(1, 6)

print('')
print('x=', x, 'y=', y, sep=' ')
print('あなたのさいころの目の合計は ',x+y)

X = randint(1, 6)
Y = randint(1, 6)

print('')
print('X=', X, 'Y=', Y, sep=' ')
print('コンピューターのさいころの目の合計は ',X+Y)

if x+y > X+Y:
    print('あなたの勝ち！')
elif x+y == X+Y:
    print('引きわけね....')
else:
    print('コンピューターの勝ちよ!!')
    
