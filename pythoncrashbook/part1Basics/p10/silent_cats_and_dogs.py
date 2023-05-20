def count_words(filename):
    """Read files"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents= f.read()
    except FileNotFoundError:
        print(f"Sorry, the {filename} does not exist")

    else:
        print(f"These are the contents of the {filename} file:")
        print(f"{contents}")

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    count_words(filename)

