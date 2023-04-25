# First off you have to import request from flask so:

from flask import Flask, render_template, request

app = Flask(__name__)

# You then add to the @app.route("/") function to say you want to be able to 
# collect infomation of it, like so:

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# You can then save text from html forms to variables like so:

# recipes[new_id] = request.form["recipe"]

# You can then collect data using the FlaskForm class, to do this you have to 
# import some more things:

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# You then make the class like so:

class CommentForm(FlaskForm):
  comment = StringField("Comment")
  submit = SubmitField("Add Comment")

# You add a variable for each bit of data you want to collect as a StringField
# with the SubmitField being what you want on the submit button. You must also
# create an instance of the class inside the function for the page. like:

@app.route("/", methods=["GET", "POST"])
def index():
    comment_form = CommentForm()
    return render_template("index.html")

# You then add the from to the HTML file like so:

<form action="/" method="post">
    {{ template_form.hidden_tag() }}
    {{ template_form.my_textfield.label }}
    {{ template_form.my_textfield() }}
    {{ template_form.my_submit() }}
</form>

# So you have to have template_form.hidden_tag for it to work, doesnt do anything
# visable its just needed for it to work. then the label will be the name of the 
# variable (if you've set one when you make it) and the normal textfield will be
# the text box that can be used to save the data.

# To collect the data you then use .data on the variable so something like:

some_var = my_textfield.data

# When collecting data you can also use things called validators, this can be 
# something like Data Required, this again needed to be imported.

from wtforms.validators import DataRequired

# Once imported you can do things like:

my_textfield = StringField("TextLabel", validators=[DataRequired()])

# To mean that the data is required for the form to be submitted and it wont take
# the data without it having something. 

# We can then also use the validate_on_submit function to check if something 
# has data in it, this could be used to, for example write:

  if comment_form.validate_on_submit():
    new_comment = comment_form.comment.data
    comments[id].append(new_comment)

# This would allow us to add something to the list of comments only if there is 
# a valid comment, prevents appending comments with just None.

# Finally we have afew more form field types. We have: TextAreaField - multi
# line string, BooleanField - yes or no box, RadioField - multi box choices. you
# write them like:

from wtforms import StringField, SubmitField, TextAreaField, RadioField

my_text_area = TextAreaField("Text Area Label")
my_checkbox = BooleanField("Checkbox Label")
my_radio_group = RadioField("Radio Group Label", choices=[("id1", "One"), 
("id2","Two"), ("id3","Three")])

# Its worth noting that the html for radio groups would look something like:

    <table><tr>
      {% for btn in template_form.recipe_type %}
      <!-- Put the button variable then the button label 
      in the following td tags-->
      <td>{{btn}}</td>
      <td>{{btn.label}}</td>
    {% endfor %}
    </tr></table>

# Oh and you can use redirect() to send someone to another page once they have 
# submitted a form, so something like

    return redirect(url_for("recipe", id=new_id, _external=True, _scheme='https'))


