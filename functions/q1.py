def inc(x):
    return x+1

def f1(list1):
    list1.append('!!!')

def main():
    x = 10
    x = inc(x)
    print(x)
    listExp = [1, 'a', 3]
    f1(listExp)
    print(listExp)

if __name__ == '__main__':
    main()
