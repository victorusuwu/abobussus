print("ЗДРАВСТВУЙТЕ вас приветствует  компания zaim bez skama228")
name = input("Как вас зовут?")

s = int(input("на какую сумму вы хотите взять займ? "+(name)))
n = int(input("сколько лет вы хотите  выплачивать проценты"+"введите число"))
p = int(input("под какой процент вы хотите взять займ? "+(name)+" введите число"))
r = p/100
print (r)
m = (s * r*(1 + r)*n) / (12 * ((1+r)*n-1))

print("каждый месяц вы должны платить"+str(m) )
