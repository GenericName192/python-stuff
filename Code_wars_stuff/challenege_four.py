# Function to check to see if there is an index in which to the right and the 
# left of the index equal each other.
def find_even_index(arr):
    for x in range(len(arr)):
        first_part = arr[:x]
        second_part = arr[x + 1:] # So the number in the index isn't inculded.
        if sum(first_part ) == sum(second_part):
            return x
    return -1 # If there is no index.

# code wars description

# You are going to be given an array of integers. Your job is to take that 
# array and find an index N where the sum of the integers to the left of N is 
# equal to the sum of the integers to the right of N. If there is no index that 
# would make this happen, return -1.