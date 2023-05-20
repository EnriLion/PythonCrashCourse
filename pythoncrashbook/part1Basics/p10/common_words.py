# line = "Row, row, row your boat"
# print(line.count('row'))
# print(line.lower().count('row'))

file = "the_yellow.txt"

with open(file, encoding='utf-8') as f:
    contents = f.read()

print(contents.lower().count('the '))
