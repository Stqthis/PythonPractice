from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template('index.html')

@views.route('/Stathis_Presentation')
def Stathis_presentation():
    return render_template('Stathis_present.html')

@views.route('/sign-up')
def sign_up():
    return render_template('signUp.html',name="stathis")