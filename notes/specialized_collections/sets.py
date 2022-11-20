# Sets are unorganized lists that cannot contain duplicates, they can writen in
# one of two ways, they can be bogstandard sets which are muteable or a frozenset
# which is inmuteable. it is written like:

example_set = set(["example_data1", "example_data2", "example_data2"])
example_frozen_set = frozenset(["random_data", "random_data2"])

# Its worth noting that while writing the above wont cause an error the set will
# only contain example_data1 and example_data2 the second example_data2 wont be
# saved.

# You can also create an empty set by writing:

empty_set = set()

# Its worth noting they can also be created using list comprehensions like:

example_2 = {category for category in example_set if category[-1] == '2'}

# To add to a set you either use add if you want to add a single element or 
# update if you want to add multiple. You write them like:

example_set.add("example_data3")
example_set.update("example_data4", "example_data5")

# There are then 2 ways to remove data from a set, you either use .remove() or
# .discard() with the only real difference being that remove will throw an 
# exception if the data isn't there. This is written as:

example_set.remove("example_data3")
example_set.discard("example_data5")

# You can also check if something is in a set same way you do a list with the in
# keyword so:

if "example_data5" in example_set:
    example_set.discard("example_data5")

# There are 4 main built in methods for sets, unions, intersections, differences
# and Symmetric Differences. Union or | combine two sets into a new one, this 
# can look like:

new_set = empty_set | example_set
# Or
new_set2 = empty_set.union(example_set)

# Intersection creates a new set that just contains the common bits of data 
# between 2 sets. Looks like:

new_set3 = new_set & example_set
# Or 
new_set4 = new_set.intersection(example_set)

# Difference creates a new set that is all of the values from the first set not
# found in the second set, basically it removes any common data from the first 
# set. It is written like:

new_set5 = new_set - example_set
# Or 
new_set6 = new_set.difference(example_set)

# finally we have symmetric difference which creates a new list that is the 
# unique data from both sets, so it deletes all common data then returns the 
# rest. Is written like:

new_set7 = new_set ^ example_set
# Or 
new_set8 = new_set.symmetric_difference(example_set)