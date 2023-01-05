# Function to remove comments from strings. (removes anything after marker.)
def strip_comments(strng, markers):
    new_string = []
    for line in strng.splitlines(): # method of string that allows me to look at the string one line at a time.
        for char in markers:
            if char in line:
                cutoff = line.index(char)
                line = line[:cutoff].rstrip() # removes anything after the found marker, then rstrips to remove any whitespace.
        new_string.append(line) # saves each line as a element in a list
                       
    return "\n".join(new_string) # joins the string back together from the list.


# code wars description 

# Complete the solution so that it strips all text that follows any of a set of 
# comment markers passed in. Any whitespace at the end of the line should also be 
# stripped out.