number = 0

def double():
    global number
    number *= 2

number = int(input("please input: "))
double()
print (number)
