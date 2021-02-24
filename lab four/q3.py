import fileinput

newfile = 'newFile.txt'

with fileinput.input(files=('userInput.txt', 'reverseuserInput.txt', 'userInputCopy.txt')) as f:
    with open(newfile, 'w') as catfile:
        for line in f:
            catfile.write(line)

with open(newfile, 'r') as fw:
    for l in fw:
        print(l, end='')

