# To start off a flask project you must first import flask and create an instance 
# of it like so:

from flask import Flask

app = Flask(__name__)

# You then use app to link functions to pages, by putting something like

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello, World!</h1>'

# You can also add variables to both the route and the text using the following 
# syntax

@app.route('/orders/<user_name>/<int:order_id>')
def orders(user_name, order_id):
    return f'<p>Fetching order #{order_id} for {user_name}.</p>'

# So <variable_name> for the URL and us an f string to pass them into text.
# Its worth noting that you can also enforce types onto variables being accepted
# by using a converter followed by a : like above. The possible converter types 
# are: 

# int: accepts positive ints
# float: accepts positive floats
# path: like string but also accepts /
# uuid: accepts UUID strings

# Its worth noting you can also add addiontal syntax inside of the {} of the f 
# string, if you wanted to convert something thats going to be a url, you may do
# something like:

@app.route('/article/<article_name>')
def article(article_name):
  return f'''
  <h2>{article_name.replace('-', ' ').title()}</h2>
  <a href='/'>Return back to home page</a>
  '''