# lambda functions are basically just one line short handed functions. an example
# would be something like:

add_two = lambda my_input: my_input + 2

# instead of 

def add_two(my_input):
  return my_input + 2

# To break this down you start by defining it the same way you would a variable,
# and then use the keyword lambda. You then put arguements you want for the 
# function then : with what you want the function to return, so in this case 
# the number thats been passed to it plus 2.

# We can also add conditionals if we want to write more complicated functions, 
# for example: 

check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'

# This would return "Got an A!" if the conitional is true and "Did not get an A"
# if the conitional is false.