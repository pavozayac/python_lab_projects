data = int(input('Enter the temperature (in Celsius): '))

if data > 35:
    print('Very hot')
elif 25 < data <= 35:
    print('Hot')
elif 15 < data <= 25:
    print('Moderate')
else:
    print('Cold')
