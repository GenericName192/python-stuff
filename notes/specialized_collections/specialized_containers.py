# All of the following are imported via collections and therefore you need to 
# start with:

from collections import *

# First up we have deque, this is type of list that is optimized for 
# appending/poping things from either the front of the back of a list. you would
# write it like: 

example_data = deque()
example_data.appendleft("add to front")
example_data.append("add to back")
example_data.popleft()
example_data.pop()

# Next up we have named tuples which are basically a cross between a tuple and a
# dictionary, you write them like:

NamedTuple = namedtuple("NamedTuple", ["first", "second", "third"])
example = NamedTuple("1st", "2nd", "3rd")
print(example.first) # Will print out 1st

# Next up we have default dictionaries, these are basically normal disctionaries
# but they have a default return if you try pull out data that isnt there. You
# write it like:

validate_prices = defaultdict(lambda: 'No Price Assigned')

validate_prices['jeans'] = 19.99
validate_prices['shoes'] = 24.99
validate_prices['t-shirt'] = 9.99
validate_prices['blouse'] = 19.99

print(validate_prices['jacket']) # Will print out No Price Assigned

# Next up we have counters, super useful stuff. allows us to easily count how, 
# many times something comes up inside a list. it is written like:

def find_amount_sold(opening, closing, item):
  opening_count = Counter(opening)
  closing_count  = Counter(closing)
  opening_count.subtract(closing_count)
  return opening_count[item]

# This would allow us to work out how many items there were less in the opening
# of a store to the closing of a store. assuming all stock was stored in a list
# for reasons.
