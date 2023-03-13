def EuclidGCD(x,y):
    if y == 0:
        return x
    r = int(x % y)
    return EuclidGCD(y,r)

def main():
    x = int(input("What's the first integer you would like to use? "))
    y = int(input("What's the second integer you would like to use? "))
    print(EuclidGCD(x,y))

if __name__ == "__main__":
    main()
