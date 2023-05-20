a = input("Give me your number: ")
b = input("Give me the second number: ")
try:
    s = int(a) + int(b)
    print(s)
except ValueError:
    print("Some of your prompt is an string")
