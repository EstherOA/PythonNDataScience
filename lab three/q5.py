def accumulator(initial, params):
    result = initial
    for i in range(len(params)):
        result += params[i]
    return result

def main():
    print("result", accumulator(0,( 1, 3, 5)))
    print("result", accumulator(5,(2, 5, 10)))
    print("result", accumulator(100,( 1, -30, 50)))

if __name__ == "__main__":
    main()