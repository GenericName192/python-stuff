# function to turn each word into pig latin
def pig_it(text):
    new_list = []
    text_list = text.split(" ") # turns the string into a list
    for x in text_list:
        if x.isalpha(): # checks to see if its a word or punctuation
            new_list.append(x[1:] + x[:1] + "ay")
        else: # so punctuation is readded untouched
            new_list.append(x)
    return " ".join(new_list) 

 
# code wars description

# Move the first letter of each word to the end of it, then add "ay" to the end 
# of the word. Leave punctuation marks untouched.