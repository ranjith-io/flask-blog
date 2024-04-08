from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']
'7db294e13aaa90ddced3878677ed6508'
posts=[
    {
        'author' :'ranjith',
        'title' :'first_blog',
        'content':'first blog created for learning',
        'date_posted':'20.03.24'
        },{
        'author':'new',
        'title':'unknown',
        'content':'second thing to write',
        'date_posted':'20.03.24'
    }
]
@app.route("/")
def hello_world():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register")
def register():
    form=RegisterForm()
    return render_template('register.html',title='register,form=form')

@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',title='Login,form=form')

if __name__ == '__main__':
    app.run(debug=True)
