#coding=utf-8


# 判断一个数是不是素数
num = int(input('请输入一个数字：'))
switch = True
for x in (2,num-1):
    if num % x == 0:
        print('这个数字不是素数！')
        switch = False
        break
if switch == True:
    print('这个数字是素数!')