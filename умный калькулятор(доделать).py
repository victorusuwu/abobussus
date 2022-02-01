num1 = input("введите с какое знак действия которое  вы хотите совершить")
first = input("введите первое число")
seck = input("введите второе число")
num2 =int(first)
num3 =int(seck)
while num1 == ("+"):
    answer = num2 + num3
    print(answer)
while num1 == ("-"):
    answer = num2 - num3
    print(answer)
while num1 == ("/"):
    answer =  num2 / num3
    print(answer)
 while num1 ==("*"):
    answer = num2 * num3
    print(answer)
    
