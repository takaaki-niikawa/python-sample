from random import randint

score = 0

for i in range(10):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    print(num1, " x ", num2, " = ", end="")
    ans = int(input())
    if ans == num1 * num2:
        score = score + 1
print("スコア＝", score, "点です") 
        
