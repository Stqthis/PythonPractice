from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)
@auth.route('/login')
def login():
    return "login"

@auth.route('/Sign-up123')
def sign_up1():
    return "Sign-Up"

@auth.route('/logout')
def logout():
    return "logout"
