import math
def amstrong_check(n):
    # Initializing to avoid garbage value in C and error in python like NameError: name 'count' is not defined
    temp1 =n
    n1 = n
    count = 0
    result = 0
    #count = math.floor(math.log10(abs(n))) + 1 if n != 0 else 1
    while n>0:
        count += 1
        n = n//10
    if n1 == 0:
        return True
    while n1 > 0 :
        extract = n1 % 10
        result = result + pow(extract,count)
        n1 = n1 // 10
    if temp1 == result:
        return True
    else:
        return False
def main():
    number = int(input("Enter a positive integer : "))
    if amstrong_check(number):
        print(f"{number} is an Armstrong number")
    else:
        print(f"{number} is not an Armstrong number")
main()