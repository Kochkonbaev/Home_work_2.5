income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]
spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]


coeff = 0
for i in range(12):
    try:
        mount = spendings[i] / income[i]
    except ZeroDivisionError:
        mount = 0
    finally:
        coeff += mount
        
print(coeff / 12)
