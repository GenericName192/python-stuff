from unicodedata import category
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import Account
from . import db 
import json

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        website = request.form.get("website")
        user_name = request.form.get("user_name")
        password = request.form.get("password")

        if len(website) < 1:
            flash("website is too short", category="error")
        elif len(user_name) < 1:
            flash("user_name is too short", category="error")
        elif len(password) < 1:
            flash("password is too short", category="error")
        else:
            new_account = Account(website=website, user_name=user_name, password=password, user_id=current_user.id)
            db.session.add(new_account)
            db.session.commit()
            flash("account added", category="success")

    return render_template("home.html", user=current_user, website="Website: ", name="Username: ", password="Password: " )


@views.route("/delete-account", methods=["POST"])
def delete_account():
    account = json.loads(request.data)
    accountId = account["accountId"]
    account = Account.query.get(accountId)
    if account:
        if account.user_id == current_user.id:
            db.session.delete(account)
            db.session.commit()

    return jsonify({})

#pass variables to the above by something like "render_template("home.html", var_name)" you can then later on use the variable by typing {{ var_name }} 