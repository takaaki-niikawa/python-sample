# 簡単な電卓
from time import sleep
while True:
    x = int(input('x='))
    y = int(input('y='))
    op = input('足し算:+ , 引き算:-, 掛け算:*, 割り算: / のいずれかを入力 =')
    if op == '+':
        z = x + y
    elif op == '-':
        z = x - y
    elif op == '*':
        z = x * y
    elif op == '/':
        z = x / y
    else:
        z = 'エラー'
    print('答えは、',z,'です')
    sleep(3)
