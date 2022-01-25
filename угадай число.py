import random 
n = random.randint(0, 10)
A = input ('угадайте число')
A = int (A)
while A != n:
   if A > n:
       print('Число СЛИШКОМ большое')
   if A < n:
       print('Число СЛИШКОМ маленькое')
   A=input ('введите число заново')
   A = int (A)
print('КАК ТЫ УГАДАЛ')


