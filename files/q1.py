
user_in = input('Enter some text and END to quit:')

try:
    f = open('userInput.txt', 'a') 
    while user_in != 'END':
        f.write(user_in + '\n')
        user_in = input('Enter some text and END to quit:')
finally: 
    f.close()

try:
    fr = open('userInput.txt', 'r') 
    i = 0
    for line in fr:
        print(i, ":", line, end='')
        i += 1
finally: 
    f.close()
