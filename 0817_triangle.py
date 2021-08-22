#coding=utf-8

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a+b>c and a+c>b and b+c>a:
    print('周长为 %.2f' % (a+b+c))
    p=(a+b+c)/2
    print('面积为 %.2f' % (p*(p-a)*(p-b)*(p-c)**0.5))
else:
    print('您输入的数据无法组成三角形')