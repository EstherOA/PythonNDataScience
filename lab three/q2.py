def reorderList(listParam):
    lastElem = listParam.pop(0)
    listParam.append(lastElem)

def main():
    listExp = [1, 'r', 9, 's']
    print('old list', listExp)
    reorderList(listExp)
    print("new list", listExp)

if __name__ == '__main__':
    main()