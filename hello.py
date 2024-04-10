from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



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