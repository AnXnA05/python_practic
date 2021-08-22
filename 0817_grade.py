score = int(input('请输入您的分数：'))
if score >= 90:
    score = 'A'
elif score >= 80:
    score = 'B'
elif score >= 70:
    score = 'C'
elif score >= 60:
    score = 'D'
else:
    score = 'E'
print(f'您的成绩是 {score}')