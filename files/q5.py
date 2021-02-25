count = 0
filename = 'userInput.txt'

with open(filename, 'r') as f:
    for line in f:
        count += 1

print("Number of lines in", filename, ":", count)