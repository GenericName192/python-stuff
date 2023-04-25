from flask import Flask, render_template

app = Flask(__name__)

# You can also pass variables to the template with something like:

descriptions = "list"
recipes = "list"
ingredients = "list"

@app.route("/recipe/<int:id>")
def recipe(id):
  return render_template("recipe.html", template_recipe = recipes[id], 
  template_description = descriptions[id], template_ingredients = ingredients[id])


# Then you can access those variables inside of the html file using something 
# like {{template_description}} or:

      # <li>{{template_ingredients[0]}}</li>
      # <li>{{template_ingredients[1]}}</li>
      # <li>{{template_ingredients[2] + "winning"}}</li>

# Its worth noting that you can also write normal python inside the {{}} to 
# add to the string or increase the int in the variable.

# You can also edit the variables further using filters, these do various things
# to the variable like putting it in uppercase, the syntax is like: 

# {{ variable | filter_name }}

# A list of all filters is as follows:

# title: Capitalizes the first letter of each word in a string, known as titlecase
# capitalize: Capitalizes the first character of a string, such as in a sentence
# lower/uppercase: Makes all the characters in a string lowercase/uppercase
# int/float: Changes any number variable to an integer/float
# default: Defines a default string if the variable is not defined
# length: Calculates the length of a string, list or dictionary variable
# dictsort: Sorts a dictionary by its keys

# You can also use if statments with the variables you pass, you write them 
# between %% and have to have an %endif% statment. it can look like:

# {% if template_number < 20 %}
#   <p>{{ template_number }} is less than 20.</p> 
# {% elif template_number > 20 %}
#    <p>{{ template_number }} is greater than 20.</p> 
# {% else %}
#    <p>{{ template_number }} is equal to 20.</p> 
# {% endif %}

# You can also do things like for loops using similar syntax. would look like:

# <ol>
# {% for x in range(3) %}
#   <li>{{ x }}</li>
# {% endfor%}
# </ol>