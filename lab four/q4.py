filename = 'userInput.txt'

with open(filename, 'r') as fr:
    with open('reverse'+filename, 'w') as fw:
        inputFile = [line for line in fr]
        inputFile.reverse()
        fw.writelines(inputFile)

with open('reverse'+filename, 'r') as revfile:
    for line in revfile:
        print(line, end='')