# スーパーの計算2

# Rate
rate = 0.9

# Sub-total
potato = int(input("じゃがいもは何個？")) * 50
carrot = int(input("にんじんは何個？")) * 80
pumpkin = int(input("かぼちゃは何個？")) * 150

# Total
sum=potato + carrot + pumpkin
print("合計　：",sum,"円になります")
print("割引後：",round(sum*0.9),"円になります")
