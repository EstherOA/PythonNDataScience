numList = []
count = 0

while count < 10:
    numElem = int(input('Enter a number between 1 and 8: '))
    if numElem > 0 or numElem < 9:
        numList.append(numElem)
        count += 1

print('You entered 5', numList.count(5), 'times')