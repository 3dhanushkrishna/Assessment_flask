from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/delete')
def delete():
    return render_template("delete.html")

if __name__=="__main__":
    app.run()