# function to return the top 3 used words
def top_3_words(text):
    answer = []
    word_count = {}
    word = ""
    valid_chars = "abcdefghijklmnopqrstuvwxyz'" # only counts these chars
    for count, x in enumerate(text, start=0):
        x = x.lower() # make it case insensitive 
        is_valid_char = x in valid_chars
        if is_valid_char:
            word += x
        if not is_valid_char or count == len(text) - 1: # checks if its a valid char or if you've reached the end of the string
            if word.count("'") == len(word): # checks to see if the word is just "'" which doesnt count as a valid word.
                word = ""
            if len(word) > 0:
                if word not in word_count: # checks to see if the word has been counted before if not adds it to the dic
                    word_count[word] = 0
                word_count[word] += 1
                word = ""
    if word_count == {}: # if no words have been found
        return answer
    sorted_dic = sorted(word_count.items(), key=lambda x:x[1], reverse=True) # sorts the dic
    for element in sorted_dic:
        answer.append(element[0])
        if len(answer) == 3: # so it only counts the first 3
            break
    return answer

 
# code wars description

# Write a function that, given a string of text (possibly with punctuation and 
# line-breaks), returns an array of the top-3 most occurring words, 
# in descending order of the number of occurrences.

# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
# Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
# Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
# Matches should be case-insensitive, and the words in the result should be lowercased.
# Ties may be broken arbitrarily.
# If a text contains fewer than three unique words, then either the top-2 or 
# top-1 words should be returned, or an empty array if a text contains no words.