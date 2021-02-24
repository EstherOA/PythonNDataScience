with open('userInput.txt', 'r') as fr:
    with open('userInputCopy.txt', 'w') as fw:
        for line in fr:
            fw.write(line)

#printing the copy
with open('userInputCopy.txt', 'r') as fcopy:
        for line in fcopy:
            print(line, end='')