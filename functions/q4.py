def getNamedParams(**kwargs):
    dictExp = {}
    print(kwargs)
    for i in kwargs.keys():
        dictExp[i+'->'] = kwargs[i]
    return dictExp

def main():
    print("Params:", getNamedParams(hello="World", up="down", start="stop", count=4))

if __name__ == "__main__":
    main()