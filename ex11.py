score1 = float(input("Enter the score for tese 1: "))
score2 = float(input("Enter the score for tese 2: "))
score3 = float(input("Enter the score for tese 3: "))
average = (score1+score2+score3) / 3
print(f'The average score is {average}')
if average > 95:
    print('Congratuions!')
    print('That is a great average!')
