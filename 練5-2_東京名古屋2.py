# 東京－名古屋間まで何時間か？
distance = 355.4
speed = 80
hour = distance / speed
min = (hour * 60) % 60
print(round(hour),"h",round(min),"min")
