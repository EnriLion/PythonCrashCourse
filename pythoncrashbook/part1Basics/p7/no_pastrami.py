unconfirmed_sandwiches = ['pastrami','chicken', 'egg','pastrami', 'seafood', 'grilled chesse', 'pastrami']

finished_sandwiches = list()

print("\nThe delu has run out of pastrami")
while 'pastrami' in unconfirmed_sandwiches:
    unconfirmed_sandwiches.remove('pastrami')


while unconfirmed_sandwiches:
    current_sandwich = unconfirmed_sandwiches.pop()

    print(f"I made your  {current_sandwich.title()} Sandwich")
    finished_sandwiches.append(current_sandwich)


print(f"The following sandwiches have been confirmed:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

