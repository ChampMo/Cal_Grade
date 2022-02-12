
sc = int(input('ใส่คะแนนของคุณ: '))
g = 0

if sc >= 80:
    g = 4.0
elif sc >= 75:
    g = 3.5
elif sc >= 70:
    g = 3.0
elif sc >= 65:
    g = 2.5
elif sc >= 60:
    g = 2.0
elif sc >= 55:
    g = 1.5
elif sc >= 50:
    g = 1.0
else: g = 0.0

print('เกรดของคุณคือ: '+ str(g))





