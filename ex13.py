hours = int(input("Enter ter number of hours worked: "))
pay = float(input("Enter the hourly pay rate: "))
if hours > 40:
    rg_hours = 40
    ovt_hours = hours - 40
    rg_pay = rg_hours * pay
    ovt_pay = ovt_hours*pay*1.5
    gross_pay = rg_pay + ovt_pay
    print(f'The gross pay is: {gross_pay}')
else:
    gross_pay = hours * pay
    print(f'The gross pay is: {gross_pay}')