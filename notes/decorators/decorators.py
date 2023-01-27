# decorators and basically just functions that add addiontal funcetionality to 
# other funections, so for example you could write a function like: 

def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("professor:")
        print_name_function()
    return wrapper

@title_decorator
def print_my_name(name):
    print(name)

# So to break down the above, first off inside of the decorator we ahve *args.
# this means it will take any number of arguments, and **kwargs which means keyword
# arguements, basically allows for the arguements to be passed to the wrapper. you
# then have whatever you want to add to the function, so in this case printing a 
# title, then you call the function you passed it. Finally you can add a decorator 
# to a function by adding @name_of_decorator above it.