pole = [['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o']]
x=0
y=0
pole[y][x]='X'

for stroka in pole:
	for kletka in stroka:
		print(kletka,end='')
	print()

while 'true':

    command=input('введите в какую сторону вы хотите сдвинутся')
    if command == 'вправо':
        pole[y][x]='o'
        x=(x+1)
        pole[y][x]='X'
        for stroka in pole:
            for kletka in stroka:
                print(kletka,end='')
            print()
    if command == 'влево':
        pole[y][x]='o'
        x=(x-1)
        pole[y][x]='X'
        for stroka in pole:
            for kletka in stroka:
                print(kletka,end='')
            print()        
 
        
    if command == 'вверх':
        pole[y][x]='o'
        y=(y-1)
        pole[y][x]='X'
        for stroka in pole:
            for kletka in stroka:
                print(kletka,end='')
            print()       

       
    if command == 'вниз':
        pole[y][x]='o'
        y=(y+1)
        pole[y][x]='X'
        for stroka in pole:
            for kletka in stroka:
                print(kletka,end='')
            print()       
	
        
print(stroka)




