def fib(maxNum): 
    fibList = []
    previousVal, currentVal = 0, 1
    count = 0

    for i in range(maxNum):
        print(previousVal)
        fibList.append(previousVal)
        accumulator = previousVal + currentVal
        previousVal = currentVal
        currentVal = accumulator
    return fibList

def main(): 
    fib(2000)
    fib(100)
    print("Fibonacci", fib(0))
    print("Fibonacci", fib(2))


if __name__ == "__main__":
    main()


    

