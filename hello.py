from flask import Flask,render_template,url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
