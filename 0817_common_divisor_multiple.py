#coding=utf-8

#输入两个正整数，计算它们的最大公约数和最小公倍数
a = int(input('请输入一个正整数：'))
b = int(input('请再次输入一个正整数：'))

if a>=b:
    numx = a
    numy = b
elif b>a:
    numx = b
    numy = a

for x in range(numy,0,-1):
    if (numx % x == 0) and (numy % x == 0):
        print(f'{x}是{a}和{b}的最大公约数')
        break
for y in range(numx,numx*numy+1):
    if y % numx == 0 and y % numy == 0:
        print(f'{y}是{a}和{b}的最小公倍数')
        break

