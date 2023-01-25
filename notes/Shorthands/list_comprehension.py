# List comprehension is just a short hand way of looping through a list. it
# follows the pattern of [EXPRESSION for ITEM in LIST <if CONDITIONAL>]. The 
# expression can be anything from just x (return as is) to x ** 3 (cube x) etc.
# item is just for each thing in the list. Finally you can add a conditional, so
# like if x > 3 etc. An example of this would be.

result = [x**2 for x in range(10) if x % 2 == 0] # This would create a list of
# all the even numbers (aswell as 0) in range 10 sqaured.