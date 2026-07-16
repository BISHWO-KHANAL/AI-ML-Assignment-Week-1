def even_odd_check(n):
    if n % 2 == 0:
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
    even_odd_check(num)
    if even_odd_check(num):
        print(f"The number \"{num}\"  is a even number.")
    else:
        print(f"The number \"{num}\" is not a even number.")
main()