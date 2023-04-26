def want_sandwich(*orders):
    """Function that accepts a list of items a person wants on a sandwich"""
    print("\nMaking a sandwich with the followed orders")
    for order in orders:
        print(f"- {order.title()}'s sandwich")

want_sandwich('chicken','egg', 'grillef')
want_sandwich('nutella')
want_sandwich('ham','seafood')

