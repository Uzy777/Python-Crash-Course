# 8-12. Sandwiches: Write a fucniton that accepts a list of items a person wants
#                   on a sandwich. The function should have one parameter that collects as
#                   many items as the function call provides, and it should print a summary
#                   of the sandwich that's being ordered. Call the function three times,
#                   using a different number of arguemnts each time.

def sandwich_order(*fillings):
    """What type of fillings do you want with your sandwich"""
    print("\nPreparing your sandwich with the following fillings:")
    for filling in fillings:
        print(filling)


sandwich_order('chicken', 'lettuce', 'tomato')
sandwich_order('beef', 'carrot', 'tomato', 'egg')
sandwich_order('fallafel', 'chicken', 'turkey ham', 'beef', 'lamb')