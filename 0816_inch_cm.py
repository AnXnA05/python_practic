num = float(input('请您输入数值：'))
unit = int(input('您输入的是（1、英寸 2、厘米）：'))
if unit == 1:
    result = num*2.54
    unit = '厘米'
elif unit == 2:
    result = num/2.54
    unit = '英寸'
else:
    result = 0
    unit = '您选择的单位类型不正确'
print(f'{result:.2f} {unit}')