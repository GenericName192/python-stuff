# Function to check if any of the words are longer then 5 letters and if they
# reverse them.
def spin_words(sentence):
    word = "" # Word being generated then checked.
    new_sentence = "" # Sentence that will be returned.
    count = 0 # Count to keep of if we're at the end of the sentence/word.
    sentence_length = len(sentence) # How long the sentence is so we can compare.
    for character in sentence:
        count += 1
        word += character
        if character == " ": # If it's hit the end of a word.
            if len(word.strip()) >= 5: # Added strip as I couldnt think of a clever way to not flip the the space 
                word = reverse_word(word) + " " # Readding the space I had to remove
            new_sentence += word
            word = ""
        if count == sentence_length: # If end of the word.
            if len(word) >= 5:
                word = reverse_word(word)
            new_sentence += word
    return new_sentence

# function I wrote to flip the word as I needed it in 2 places and didnt want to rewrite it.
def reverse_word(word):
    return word[::-1].strip()


# code wars description

# Write a function that takes in a string of one or more words, and returns the 
# same string, but with all five or more letter words reversed (Just like the 
# name of this Kata). Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.