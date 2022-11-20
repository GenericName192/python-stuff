# First off we have raising exceptions, do this using the raise keyword like:
def test():
    raise NameError('Custom Message')

# Its worth notinhg that you don't need the brackets you only add them if you 
# want to add a custom message.

# Second we have try statements, this is basically were you tell it to try run
# the code and you use except statements to catch the errors. its worth noting 
# that you can use this to catch general errors or specific ones, looks like:

try:
    print("David is great")
except NameError:
    print("I guess David isnt so great afterall")

# You can also use this to catch more then one error and even print out the 
# error by using as, this looks like:

try:
    print("David is great")
except (NameError, TypeError) as error:
    print(error)

# Its worth noting you can also add onto this the else keyword and the finally
# keyword like so.

try:
    print("David is great")
except:
    print("I guess David isnt so great afterall")
else:
    print("Search your feelings you know it to be true")
finally:
    print("something something darkside")

# The way this works is the computer will try and run the try statement and if
# it is successful it will run the else block, it will then regardless of if it 
# hit the exception or not carry out the finally block.

# Lastly we have user-defined exceptions, you do this by creating a class that
# inherits from the Exception clas like so:

class Custom_error(Exception):
  
  def __init__(self, distance):
    self.distance = distance

  def __str__(self):
    return "Location is not within the allowed distance:" + str(self.distance)

# This would mean we could raise the custom_error and it would print out the 
# __str__ error message.