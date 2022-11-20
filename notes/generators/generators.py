# Generators are functions that allow use to make iterator objects without 
# having to implement __iter__() or __next__(). It does this through the use of 
# the keyword yield, unlike return which gives all of the data back at once, 
# yield tends to give one bit at a time and we use a for loop to get each one. 
# yield will also suspend the execution of the function and preserve any local 
# variables. A simple generator function could look like: 

def class_standing_generator():
  yield "Freshman"
  yield "Sophomore"
  yield "Junior"
  yield "Senior"

class_standings = class_standing_generator()

for standing in class_standings:
  print(standing)

# You could also next() through it instead of the for loop.

# Its worth noting that you can also use syntax similar to list comprehensions
# to shorthand generator expressions, with the difference being: 

# List comprehension
a_list = [i*i for i in range(4)]
 
# Generator comprehension
a_generator = (i*i for i in range(4))

# Heres and example of how this can work: 

def cs_generator():
  for i in range(1,5):
    yield "Computer Science " + str(i)

# Is the same as:

cs_generator_exp = ("Computer Science {}".format(i) for i in range(1,5))

# Next up we have send() which allows us to send data to the the next yield 
# inside a generator function. This looks like: 

def count_generator():
  while True:
    n = yield
    print(n)
 
my_generator = count_generator()
next(my_generator) # 1st Iteration Output: (This is because the yield happens
#before the print statement.)
next(my_generator) # 2nd Iteration Output: None
my_generator.send(3) # 3rd Iteration Output: 3
next(my_generator) # 4th Iteration Output: None

# You can also use throw() to raise exceptions, so something like:
 
my_generator.throw(ValueError, "Bad value given")

# You can also use close() to force the function to stop regardless of how far 
# along it is. This looks like:

my_generator.close()

# Finally we can connect generators, we can do this is one of 2 ways, first up 
# is yield from, which basically allows us to pass a yield from one function to 
# another, this could look like: 

def cs_courses():
    yield 'Computer Science'
    yield 'Artificial Intelligence'
 
def art_courses():
    yield 'Intro to Art'
    yield 'Selecting Mediums'
 
 
def all_courses():
    yield from cs_courses()
    yield from art_courses()

print(next(all_courses))
print(next(all_courses))
print(next(all_courses))
print(next(all_courses))

# With the output being:

# Computer Science
# Artificial Intelligence
# Intro to Art
# Selecting Mediums

# The second way is to create generator pipelines this is were a generator takes
# another generator as an argument. Could look like:

def number_generator():
  i = 0
  while True:
    yield i
    i += 1
 
def even_number_generator(numbers):
  for n in numbers:
    if n % 2 == 0:
      yield n

even_numbers = even_number_generator(number_generator())