def selectFromList(list1, *listIndices):
    results = []
    for i in range(len(listIndices)):
        currentIndex = listIndices[i]
        results.append(list1[currentIndex])

    return tuple(results)

def main():
    listExp = ['a', 'e', 'i', 'o', 'u']
    print("Selected", selectFromList(listExp, 1, 0, 4, 2))

if __name__ == "__main__":
    main()