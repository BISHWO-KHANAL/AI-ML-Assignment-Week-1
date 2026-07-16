def prime_check(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count == 2:
         return True
    else:
        return False
def main():
    while True:
     try:
      num = int(input("Enter a number: "))
      break
     except ValueError:
        pass
    prime_check(num)
    if prime_check(num):
        print(f"The number \"{num}\"  is a prime number.")
    else:
        print(f"The number \"{num}\" is a composite number.")
main()