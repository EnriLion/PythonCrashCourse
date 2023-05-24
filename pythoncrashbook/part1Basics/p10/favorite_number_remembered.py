import json

def read_favorite_number():
    """Read favorite number"""
    filename = 'favorite.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def favorite_number():
    """Create favorite number"""
    number = input("What is your favorite number? " )
    file = 'favorite.json'
    with open(file, 'w') as f:
        json.dump(number, f)
    return number

def main():
    """Create favorite number or read it"""
    number = read_favorite_number()
    if number:
        print(f"I know your favorite number!, It's {number}")
    else:
        number = favorite_number()

main()


