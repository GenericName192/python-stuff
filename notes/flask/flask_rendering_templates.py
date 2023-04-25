# So to use HTML files in flask you have to import the function render_template
# so you just import it along with Flask like so:
from flask import Flask, render_template

app = Flask(__name__)

# You then just make the function normally but instead of returning a string you 
# you return the funection like so:

@app.route('/')
def index():
  return render_template("index.html")

# You can also have things render across more then one template by inheritance, 
# you do this by first defining where you want inherited code like:

  # <body>
  # {% block content %}{% endblock %}
  # </body>

# You then in the second file you put:

# {% extends "base.html"  %}

# At the top then whatever you want to be across all pages like:

# {% block content %}
#     <p>This is my paragraph for this page.</p>
# {% endblock %}