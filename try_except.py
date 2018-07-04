def add_numbers(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("Please input integer.")
    return x + y


try:
    a = int(input("Input a number: "))
    print(add_numbers(a, 7))
except:
    print("you got it wrong, but here's the secret anyway")
print("the secret is: wows")
