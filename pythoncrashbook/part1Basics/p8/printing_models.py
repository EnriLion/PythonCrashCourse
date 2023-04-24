##Modifiying a list in a function

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot', 'dodecahedron']
completed_models = []

# Simulate a priting each design , until none are left
#  Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Display all completed models

print(f"\n The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#We could reorganize the code to make easi to understand

print("\n")
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print(f"\n The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a function from modifying a list

#You may decide even tough you've printed all the designs, you want  to keep the original list of unprinted_designs 

#Any changes the function makes to the list  will affect only the copy, leaving the original list intact

# function_name(list_name[:])

#The slice notation [:] makes a copy of the list tp send to the function. If we didn't want to empty the list of unprinted designs in printing_models.py we could call() print_models like this:

# print_models(unprinted_designs[:], completed_models)

#its more efficient for a function to work with an existing list to avoid using the time and memory need to make a separate copy, especially when you're working with large lists

