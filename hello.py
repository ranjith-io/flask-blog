from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db= SQLAlchemy(app)

class user(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=True)
    password=db.Column(db.String(60),nullable=False)
    post=db.relationship('Post',backref='author',lazy=True)

    def __repr__(self) :
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class post(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title =db.Column(db.String(100),nullable=False)
    date_posted =db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,nullable=False)

    def __repr__(self) :
        return f"Post('{self.title}','{self.date_posted}')"

posts=[
    {
        'author' :'ranjith',
        'title' :'first_blog',
        'content':'first blog created for learning',
        'date_posted':'20.03.24'
        },{
        'author':'new',
        'title':'Mine',
        'content':'second thing to write',
        'date_posted':'20.03.24'
    }
]
@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods =['GET','POST'] )
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='register',form=form)

@app.route("/login",methods =['GET','POST'] )
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in' ,'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessfull . Please check username or password','danger')
    return render_template('login.html',title='Login',form=form)

if __name__ == '__main__':
    app.run(debug=True)