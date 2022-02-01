points = input("введите сумму вашей покупки")
points = int(points)
max = int(1000)
ballance=(points)/10
plus = int(0)
total = ballance + plus
while total < max:
    print("ваш балланс составляет",total)
    points = input("введите сумму вашей покупки")
    points = int(points)
    plus=(points)/10
    total = ballance + plus
print("БАЛЛЫ НАКОПЛЕНЫ ВРЕМЯ ТРАТИТЬ!!!")