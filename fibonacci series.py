def generatefibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return generatefibonacci(n-1) + generatefibonacci(n-2)
def main():
    while True:
        try:
            number = int(input("Enter how many numbers you want: "))
            if number <= 0:
                print("Please enter a positive number! and term greater than 0!!")
            else:
                break
        except ValueError:
            pass
    print("The fibonacci result is : ",generatefibonacci(number))
main()


