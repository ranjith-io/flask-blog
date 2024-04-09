from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

<<<<<<< HEAD
app.config['SECRET_KEY']='7db294e13aaa90ddced3878677ed6508'
=======
app.config['SECRET_KEY']
'7db294e13aaa90ddced3878677ed6508'
>>>>>>> e12b2823143e5c17f9faae186344bcfb969480f8
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
<<<<<<< HEAD
def home():
=======
def hello_world():
>>>>>>> e12b2823143e5c17f9faae186344bcfb969480f8
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register")
def register():
<<<<<<< HEAD
    form=RegistrationForm()
    return render_template('register.html',title='register',form=form)
=======
    form=RegisterForm()
    return render_template('register.html',title='register,form=form')
>>>>>>> e12b2823143e5c17f9faae186344bcfb969480f8

@app.route("/login")
def login():
    form=LoginForm()
<<<<<<< HEAD
    return render_template('login.html',title='Login',form=form)
=======
    return render_template('login.html',title='Login,form=form')
>>>>>>> e12b2823143e5c17f9faae186344bcfb969480f8

if __name__ == '__main__':
    app.run(debug=True)
