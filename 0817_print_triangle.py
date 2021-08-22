#绘制圣诞树

num = int(input('请输入您要绘制的圣诞树层数：'))

for x in range(1,num+1):
    for _ in range(x):
        print('*',end='')
    print()

for x in range(1,num+1):
    for _ in range(num-x):
        print(' ',end='')
    for _ in range(x):
        print('*',end='')
    print()

if num % 2 != 0:
    for x in range(1,num+1,2):
        y = int((num-x)/2)
        for _ in range(y):
            print(' ',end='')
        for _ in range(x):
            print('*',end='')
        for _ in range(y):
            print(' ',end='')
        print()