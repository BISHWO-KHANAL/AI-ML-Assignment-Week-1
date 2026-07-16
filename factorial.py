def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def main():
    while True:
        try:
            num = int(input("Enter a number whose factorial you want: "))
            if num < 0:
                print("Please enter a positive number!!!")
            else:
                break
        except ValueError:
            pass
    print("Factorial is: ", factorial(num))
main()