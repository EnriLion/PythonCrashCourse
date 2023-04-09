favorite_number = {
        'john': 4,
        'gerard': 10,
        'george': 11,
        'zlatan': 777,
        }

print(f"There are many people around there as you John because your favorite number is {favorite_number['john']}")
print("\n")
print(f"There are many people around there as you Gerard because your favorite number is {favorite_number['gerard']}")
print("\n")
print(f"There are many people around there as you George because your favorite number is {favorite_number['george']}")
print("\n")
print(f"There are many people around there as you Zlatan because your favorite number is {favorite_number['zlatan']}")

favorite_numbers = {
        'john': [4, 5, 8],
        'gerard': [9, 10, 11],
        'george': [1, 2, 5, 6, 0],
        'zlatan': [777, 50, 9, 99],
        }

for names, numbers in favorite_numbers.items():
    print(f"\n{names.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")

