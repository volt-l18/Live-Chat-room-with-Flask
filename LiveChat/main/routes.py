from flask import render_template, Blueprint

main = Blueprint('main' , __name__)

@main.route("/", methods = ['GET', 'POST'])
@main.route("/home", methods = ['GET', 'POST'])
def home():
    return render_template('home.html')
