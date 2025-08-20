print('KPH \t MPH')
print('---------------')
for KPH in range(60,140,10):
    MPH = KPH*0.6214
    print(f'{KPH}\t{MPH:.2f}')