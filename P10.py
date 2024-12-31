year=int(input('Enter Year: '))

if year%4==0 and year%100!=0:
    print('leap year')
elif year%100==0 and year%400==0:
    print('leap year')
else:
    print('Not a leap year')
