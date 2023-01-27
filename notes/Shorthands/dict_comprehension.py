# Like with lists there is also a way of shorthand making a Dict but due to, 
# needing both a key and a value you do this by combining two lists into a dict. 
# it can be written like:

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = {key:value for key, value in zip(drinks, caffeine)}

# this would combine a list of names with a list of heights to create a dict like:

{'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}