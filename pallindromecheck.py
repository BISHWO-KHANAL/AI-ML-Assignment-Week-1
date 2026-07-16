def pallindrome_check(n):
    temp = n
    add = 0
    while n > 0:
        extract = n % 10
        add = add * 10  + extract
        n = n // 10
    if temp == add:
        print(f"The number {temp} is a pallindrome...")
    else:
        print(f"The number {temp} is not a pallindrome number !!!")

def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            pass
    pallindrome_check(num)
main()