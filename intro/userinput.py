#prompt user for number
num = int(input('Please enter a number: '))
#print message if odd/even
if num % 2 == 0:
    print(num, 'is an even number')
else: 
    print(num, 'is an odd number')