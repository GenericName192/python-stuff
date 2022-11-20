# an iterable is anything that can be looped through, one element at a time, this
# can be anything from a list to a string. You can loop through these things 
# easily by using something like a for loop. for loops work by first calling 
# iter() or __iter__ to create an iterator object then uses next() or __next__
# to go through each line, it will keep doing this with each next() untill it 
# hits a StopIteration exception which forces the loop to end.

# If you wanted to make a class an iterable object you can do this by defining
# __iter__() and __next__() inside it otherwise it wont work. For example:

class CustomerCounter:
  def __iter__(self):
    self.count = 0
    return self

  def __next__(self):
    self.count += 1
    if self.count > 100:
      raise StopIteration
    else:
      return self.count

customer_counter = CustomerCounter()

for x in customer_counter:
  print(x)

# This would allow you to count up to 100 and would stop there due to the 
# StopIteration. 

# Python gives some useful build in iterators you can access through importing
# itertools. First up we have count:

import itertools
 
for i in itertools.count(start=0, step=2):
  print(i)
  if i >= 20:
    break

# This would count from whatever start is, so in this case 0 in steps of 2, so 
# would print out 0, 2, 4 etc untill it hits 20. 

# Next up we have chain():

odd = [5, 7, 9]
even = {6, 8, 10}
 
all_numbers = itertools.chain(odd, even)

# Chain will combine two iterator objects together into one, it does so without
# an order tho so all_numbers may not be 5, 6, 7, etc

# Finally we have combinations: 

collars = ["Red-S","Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

collar_combo_iterator = itertools.combinations(collars, 3)

# This will return an iterator object that contains a series of tuples which 
# contain the possible combinations of in this case 3 collars. You can then get
# this data using a for loop, in this case the data would look like: 

# ('Red-S', 'Red-M', 'Blue-XS')
# ('Red-S', 'Red-M', 'Green-L')
# ('Red-S', 'Red-M', 'Green-XL')
# ('Red-S', 'Red-M', 'Yellow-M')
# etc