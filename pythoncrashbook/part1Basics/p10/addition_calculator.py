while True:
    a = input("Give me your number: ")
    if a == 'q' or a == 'Q':
        break
    b = input("Give me the second number: ")
    if b == 'q' or b == 'Q':
        break
    try:
        s = int(a) + int(b)
        print(s)
    except ValueError:
        print("Some of your prompt is an string or both")
