from flask import Flask, render_template,request
import sqlite3

data= sqlite3.connect("student.db",check_same_thread=False)
table=data.execute("select name from sqlite_master where type='table' and name='studentdata'").fetchall()
if table !=[]:
    print("table already created")
else:
    data.execute('''create table studentdata(
    ID integer primary key autoincrement,
    Name text,
    Branch text,
    Rollno integer,
    Admno integer,
    Dob text,
    Pass text,
    semester text
);''')
    print("table created")

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=="POST":
        getName=request.form["name"]
        getBranch=request.form["Branch"]
        getAdmno=request.form["AdmNo"]
        getRollno=request.form["Rollno"]
        getDob=request.form["dob"]
        getSem=request.form["Semester"]
        getPass=request.form["password"]
        getConPass=request.form["confirm_password"]
        print(getName)
        print(getBranch)
        print(getAdmno)
        print(getRollno)
        print(getDob)
        print(getSem)
        print(getPass)
        print(getConPass)
        try:
            query="insert into studentdata(Name,Branch,Rollno,Admno,Dob,Pass,semester) \
                         values('"+getName+"','"+getBranch+"',"+getRollno+","+getAdmno+",'"+getDob+"','"+getPass+"','"+getSem+"')"
            print(query)
            data.execute(query)
            data.commit()
            data.close()
            print("data added successfully")
        except Exception as err:
            print("error occured",err)
    return render_template("register.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/delete')
def delete():
    return render_template("delete.html")

if __name__=="__main__":
    app.run()